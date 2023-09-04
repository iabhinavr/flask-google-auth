# Google OAuth with Flask

This project shows how to setup OAuth2 authentication with Google OAuth2 OpenID Connect in a Flask application.

If you are cloning the repo, don't forget to create an .env file with the following values:

```
GOOGLE_CLIENT_ID="1234-your-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="ABCD-your-client-secret"
GOOGLE_REDIRECT_URI="http://localhost:5000/google/callback"
```