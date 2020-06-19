from flask import Flask, jsonify, request
from flask.views import MethodView
from marshmallow import ValidationError


from schemas import user_create_schema, user_schema
from services import UsersService


class UsersView(MethodView):
    def post(self):
        request_json = request.json
        try:
            user_create = user_create_schema.load(request_json)
        except ValidationError as e:
            return jsonify(e.messages), 400
        else:
            service = UsersService()
            user = service.create_user(user_create)
            return jsonify(user_schema.dump(user)), 201


app = Flask(__name__)
app.add_url_rule('/users', view_func=UsersView.as_view('users'))
