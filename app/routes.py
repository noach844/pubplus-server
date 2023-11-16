from app import app
from app.views import auth_bp

app.register_blueprint(auth_bp)
