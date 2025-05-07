# service-track/backend/app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request, jsonify
from routes.tickets import ticket_bp
from routes.users import user_bp
import os

app = Flask(__name__, template_folder='templates')
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tickets.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'admin', 'tech', 'user'
    tickets = db.relationship('Ticket', backref='submitter', lazy=True)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='open')  # open, in_progress, closed
    priority = db.Column(db.String(20), default='medium')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# API Endpoints
@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'status': t.status,
        'priority': t.priority,
        'user_id': t.user_id,
        'timestamp': t.timestamp
    } for t in tickets])

@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    ticket = Ticket(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'open'),
        priority=data.get('priority', 'medium'),
        user_id=data['user_id']
    )
    db.session.add(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket created', 'id': ticket.id}), 201

@app.route('/api/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json()
    ticket = Ticket.query.get_or_404(ticket_id)

    ticket.title = data.get('title', ticket.title)
    ticket.description = data.get('description', ticket.description)
    ticket.status = data.get('status', ticket.status)
    ticket.priority = data.get('priority', ticket.priority)

    db.session.commit()
    return jsonify({'message': 'Ticket updated'})

@app.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket deleted'})

# UI Route
@app.route('/tickets')
def ticket_table():
    open_tickets = Ticket.query.filter_by(status='open').all()
    working_tickets = Ticket.query.filter_by(status='working').all()
    finished_tickets = Ticket.query.filter_by(status='finished').all()
    return render_template(
        'ticket_table.html',
        open_tickets=open_tickets,
        working_tickets=working_tickets,
        finished_tickets=finished_tickets
    )

# Register Blueprints
app.register_blueprint(ticket_bp, url_prefix='/api/tickets')
app.register_blueprint(user_bp, url_prefix='/api/users')

print("Running app.py...")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

