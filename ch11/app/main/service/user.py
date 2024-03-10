import datetime
from app.main import db
from app.main.model.user import User


class UserService:
    def save_new_user(self, data):
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            new_user = User(
                email=data["email"],
                username=data["username"],
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow(),
            )
            self.save_changes(new_user)
            response_object = {
                "status": "success",
                "message": "Successfully registered.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "User already exists. Please Log in.",
            }
            return response_object, 409

    def get_all_users(self):
        return User.query.all()

    def get_a_user(self, username):
        return User.query.filter_by(username=username).first()

    def save_changes(self, data: User):
        db.session.add(data)
        db.session.commit()
