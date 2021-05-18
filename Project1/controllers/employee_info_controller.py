from flask import jsonify

from services.employee_info_service import EmployeeInfoService


def run(app):

    @app.route("/login/<employee_id>/info", methods=["GET"])
    def get_employee_info(employee_id):
        return jsonify(EmployeeInfoService.get_employee_info_by_id(employee_id))

