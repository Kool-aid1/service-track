from flask import Blueprint

ticket_bp = Blueprint('ticket_bp', __name__)

@ticket_bp.route('/')
def ticket_home():
    return "Ticket route is working!"
