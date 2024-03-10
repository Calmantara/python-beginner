from app.main import db, ma


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, username, created_at, updated_at) -> None:
        super().__init__()
        self.email = email
        self.username = username
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
