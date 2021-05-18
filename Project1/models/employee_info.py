

class EmployeeInfo:

    def __init__(self, fname="", lname="", id=0, erole=""):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.erole = erole

    def json(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "id": self.id,
            "erole": self.erole
        }

    @staticmethod
    def json_parse(json):
        employee = EmployeeInfo()
        employee.fname = json["fname"]
        employee.lname = json["lname"]
        employee.id = json["id"]
        employee.erole = json["erole"]
        return employee

    def __repr__(self):
        return str(self.json())

