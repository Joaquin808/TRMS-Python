from daos.form_dao import FormDAO
from services.form_service import FormService


class FormTest:

    @staticmethod
    def submitting_form_test(form):
        return FormService.submit_form(form=form)
