from odoo import api, fields, models


class HrJob(models.Model):
    _inherit = "hr.job"

    affordable_salary = fields.Integer(string="Affordable Salary")
