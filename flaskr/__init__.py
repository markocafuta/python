from flaskr.task1 import task1
from flaskr.task2 import task2
from flask import Flask
from werkzeug.exceptions import InternalServerError


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(task1.task1_bp)
    app.register_blueprint(task2.task2_bp)
    app.register_error_handler(400, handle_400)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(415, handle_415)
    app.register_error_handler(InternalServerError, handle_500)
    return app


def handle_400(e):
    return str(e).replace("400 Bad Request: ", ""), 400


def handle_404(e):
    return "404 Not Found", 404


def handle_415(e):
    return str(e), 415


def handle_500(e):
    original = getattr(e, "original_exception", None)

    if original is None:
        return f"500 Internal server error", 500

    return f"500 Internal server error: {str(original)}", 500
