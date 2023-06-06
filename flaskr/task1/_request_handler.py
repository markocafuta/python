from flask import request, abort
from flaskr.task1._full_name_joiner import _FullNameJoiner


class _RequestHandler:

    def handle_request(self):
        self.__validate_request()
        return self.__handle_request()

    @staticmethod
    def __handle_request():
        try:
            return _FullNameJoiner().join_names(request.json)
        except ValueError as e:
            abort(400, e)

    @staticmethod
    def __validate_request():
        if not request.is_json:
            abort(415, "Invalid request! Request should contain JSON body.")
