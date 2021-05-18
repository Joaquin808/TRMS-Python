

class GradingFormat:

    def __init__(self, grading_type, letter_grades, pass_grades):
        self.grading_type = grading_type
        self.letter_grades = letter_grades
        self.pass_grades = pass_grades

    def json(self):
        return {
            "gradingType": self.grading_type,
            "letterGrades": self.letter_grades,
            "passGrades": self.pass_grades
        }

    @staticmethod
    def json_parse(json):
        format = GradingFormat()
        format.grading_type = json["gradingType"]
        format.letter_grades = json["letterGrades"]
        format.pass_grades = json["passGrades"]
        return format

    def __repr__(self):
        return str(self.json())

