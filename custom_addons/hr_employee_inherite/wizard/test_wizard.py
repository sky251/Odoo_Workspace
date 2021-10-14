from odoo import api, fields, models


class Wizardtest(models.TransientModel):
    _name = "hr.seq.wizard"
    _description = "Hr Employee Wizard"
    _rec_name = "name"

    name = fields.Char()

    def test_wizard(self):
        context = self._context
        employee = self.env["hr.employee"].browse(context["active_id"])
        employee.mobile_phone = self.name
