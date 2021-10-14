from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    sequence = fields.Char()

    @api.model
    def create(self, vals):
        vals["sequence"] = (
            self.env["ir.sequence"].next_by_code("hr.employee.sequence.code") or "New"
        )
        return super(HrEmployee, self).create(vals)
