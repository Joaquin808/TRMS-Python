from models.login import Login
from services.login_service import LoginService
from flask import jsonify, request


def run(app):

    # @app.route("/login", methods=["POST"])
    # def post_login():
    #     LoginService.create_login(request.json)
    #     return "", 200

    @app.route("/login", methods=["POST"])
    def employee_login():
        try:
            login = Login.json_parse(request.json)
            e_login = LoginService.employee_login(login)
            return jsonify(e_login), 200
        except TypeError:
            return "Username or Password is incorrect, please try again", 404
