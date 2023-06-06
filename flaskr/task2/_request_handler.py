from flask import request, abort
from flaskr.task2._braces_checker import _BracesChecker, _UnbalancedBracesError


class _RequestHandler:

    def handle_request(self):
        self.__validate_request()
        return self.__check_if_balanced(request.data.decode('utf-8'))

    @staticmethod
    def __check_if_balanced(text):
        try:
            return _BracesChecker(text).check_if_balanced()
        except _UnbalancedBracesError as e:
            return abort(400, f"{str(e)} << brace is unbalanced.")

    @staticmethod
    def __validate_request():
        if not request.content_type == "text/plain":
            abort(415, "Invalid request! Content type of a request should be text/plain.")
