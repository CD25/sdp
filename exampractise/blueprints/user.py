from flask import Blueprint

auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/signup", methods=["POST"])
def post_new_user():
    """Api to register new user"""
    return "CREATED", 201


@auth_blueprint.route("/login", methods=["POST"])
def user_login():
    """Api to authenticate and generate
    JWT token and redirect to homepage"""
    return "OK", 200


@auth_blueprint.route("/logout", methods=["POST"])
def user_logout():
    """Api to logout user and remove JWT token"""
    return "SUCCESSFUL", 200
