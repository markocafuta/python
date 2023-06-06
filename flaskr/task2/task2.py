from flask import Blueprint
from flaskr.task2._request_handler import _RequestHandler

task2_bp = Blueprint('task2', __name__, url_prefix='/task2')


@task2_bp.route('/', methods=['POST'])
def task2():
    return _RequestHandler().handle_request()
