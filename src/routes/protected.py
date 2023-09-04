from flask import Blueprint, render_template, request
import requests

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected')
def protected():
    authenticated = False
    user_data = []

    if 'oauth_tuts_google_access_token' in request.cookies:

        access_token = request.cookies.get('oauth_tuts_google_access_token')
        api_url = 'https://openidconnect.googleapis.com/v1/userinfo'

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Accept': 'application/json'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            if all(key in user_data for key in ['sub', 'name', 'given_name', 'picture', 'email']):
                authenticated = True
    
    return render_template("protected.html", authenticated=authenticated, user_data=user_data)