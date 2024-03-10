from flask import request
from flask_restx import Resource

from app.main.util.dto import UserDto
from app.main.service.user import UserService
from app.main.model.user import UserSchema

api = UserDto.api
_user = UserDto.user

userSvc = UserService()


@api.route("/")
class UserList(Resource):
    @api.doc("list_of_registered_users")
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """List all registered users"""
        return userSvc.get_all_users()

    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data = request.json
        return userSvc.save_new_user(data=data)
