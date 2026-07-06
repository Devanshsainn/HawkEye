from flask import Flask

from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    """
    Application Factory.

    Creates and configures the HawkEye Flask application.
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    # Register Blueprints
    from app.routes.home import home_bp

    app.register_blueprint(home_bp)

    return app