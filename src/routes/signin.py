from flask import Blueprint, render_template
from dotenv import load_dotenv
import os

signin_bp = Blueprint('signin', __name__)

load_dotenv()

@signin_bp.route('/signin')
def google_signin():
    
    google_vars = {
        'google_client_id': os.getenv('GOOGLE_CLIENT_ID'),
        'google_client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
        'google_redirect_uri': os.getenv('GOOGLE_REDIRECT_URI')
    }
    return render_template("signin.html", google_vars=google_vars)