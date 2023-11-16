from app import app
from app.views import auth_bp, status_bp, user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(status_bp)
app.register_blueprint(user_bp)
