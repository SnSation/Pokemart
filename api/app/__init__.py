from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
# login = LoginManager()

def create_app(config_file=Config):
    app = Flask(__name__)
    app.config.from_object(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    # login.init_app(app)

    from .blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
