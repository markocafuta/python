from flask import Blueprint
from flaskr.task1._request_handler import _RequestHandler

task1_bp = Blueprint('task1', __name__, url_prefix='/task1')


@task1_bp.route('/', methods=['POST'])
def task1():
    return _RequestHandler().handle_request()
