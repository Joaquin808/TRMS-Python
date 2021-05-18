from flask import jsonify, request
from models.form import Form
from services.form_service import FormService


def run(app):

    @app.route("/login/<employee_id>/form", methods=["GET"])
    def get_all_forms_for_employee(employee_id):
        #  Used to change the data type time into a string so it can be jsonified properly
        # form = json.dumps(FormService.get_all_forms_for_employee(int(employee_id)), default=str)
        form = FormService.get_all_forms_for_employee(int(employee_id))
        return jsonify(form)

    @app.route("/login/<employee_id>/form", methods=["POST"])
    def submit_form_for_approval(employee_id):
        form = Form.json_parse(request.json)
        form.employee_id = employee_id
        submitted_form = FormService.submit_form(form)
        return jsonify(submitted_form)

    @app.route("/login/<employee_id>/approve", methods=["PUT"])
    def approve_form(employee_id):
        form = Form.json_parse(request.json)
        return jsonify(FormService.approve_form(form, employee_id)), 200

    @app.route("/login/<employee_id>/request", methods=["PUT"])
    def request_info(employee_id):
        form = Form.json_parse(request.json)
        return jsonify(FormService.request_info(form, employee_id)), 200


