from flask_restx import Namespace, fields


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "created_at": fields.DateTime(description="user created at"),
            "updated_at": fields.DateTime(description="user updated at"),
        },
    )
