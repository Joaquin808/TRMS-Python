

class Roles:

    def __init__(self, role_type):
        self.role_type = role_type

    def json(self):
        return {
            "roleType": self.role_type
        }

    @staticmethod
    def json_parse(json):
        role = Roles()
        role.role_type = json["roleType"]
        return role

    def __repr__(self):
        return str(self.json())

