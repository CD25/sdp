import enum

from exampractise import db


class UserType(enum.Enum):
    STUDENT = "student"
    ADMIN = "admin"


class User(db.Model):
    username = db.Column(db.String(120), primary_key=True, nullable=True)
    email = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    usertype = db.Column(
        db.Enum(UserType), nullable=True, default=UserType.STUDENT.value
    )
    user_token = db.relationship("AuthToken", backref="user")

    def __repr__(self):
        return "<User %r>" % self.username

    def __name__(self):
        return "User"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "usertype": self.usertype,
        }


class AuthToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=True)
    expiry_time = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.username"))

    def __repr__(self):
        return "<AuthToken %r>" % self.token

    def __name__(self):
        return "AuthToken"
