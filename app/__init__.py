from flask import Flask

from config import config


def create_app(config_name: str = "default") -> Flask:
    """
    Flask Application Factory.

    Parameters
    ----------
    config_name : str
        Configuration profile.

    Returns
    -------
    Flask
        Configured Flask application.
    """

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    app.config.from_object(
        config.get(
            config_name,
            config["default"]
        )
    )

    register_blueprints(app)

    register_error_handlers(app)

    return app


def register_blueprints(app: Flask) -> None:
    """
    Register Flask blueprints.
    """

    from app.routes.home import main_bp
    from app.routes.scan import scan_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(scan_bp)
def register_error_handlers(app: Flask) -> None:
    """
    Register application-wide error handlers.
    """

    @app.errorhandler(404)
    def page_not_found(error):
        return (
            "<h1>404</h1>"
            "<p>The requested page could not be found.</p>",
            404,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            "<h1>500</h1>"
            "<p>An internal server error occurred.</p>",
            500,
        )