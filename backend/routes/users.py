from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def user_home():
    return "User route is working!"
