from daos.login_dao import LoginDAO
from models.login import Login


class LoginTest:

    @staticmethod
    def test_login(username, password):
        login = Login(username=username, password=password, id=0)
        return LoginDAO.employee_login(login)
