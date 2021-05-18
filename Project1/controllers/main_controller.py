from controllers import form_controller as cc
from controllers import employee_info_controller as ec
from controllers import grading_format_controller as gc
from controllers import login_controller as lc
from controllers import roles_controller as rc
from controllers import type_of_event_controller as tc


def run(app):
    cc.run(app)
    ec.run(app)
    gc.run(app)
    lc.run(app)
    rc.run(app)
    tc.run(app)
