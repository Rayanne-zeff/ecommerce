from flask import Flask
from .extensions import db, login_manager, cors
from .models import User
from .routes import auth_bp, products_bp, cart_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)   # Carrega as configs do config.py

    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    # Rotas
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)

    @app.route('/')
    def index():
        return 'API up'

    return app