from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
import os
import requests

google_callback_bp = Blueprint("google_callback", __name__)

load_dotenv()

@google_callback_bp.route('/google/callback')
def google_callback():
    if 'code' in request.args:
        code = request.args.get('code')
        client_id = os.getenv('GOOGLE_CLIENT_ID')
        client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')

        token_data = exchange_code_for_token(code, client_id, client_secret, redirect_uri)

        if 'access_token' in token_data:

            access_token = token_data['access_token']

            response = redirect(url_for('index'))
            response.set_cookie('oauth_tuts_google_access_token', access_token, httponly=True)
            return response
        
    return 'OAuth2 callback failed'
    
def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    token_data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    response = requests.post('https://oauth2.googleapis.com/token', data=token_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {}