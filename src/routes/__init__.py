from .signin import signin_bp
from .google_callback import google_callback_bp
from .protected import protected_bp

def register_blueprints(app):
    app.register_blueprint(signin_bp)
    app.register_blueprint(google_callback_bp)
    app.register_blueprint(protected_bp)