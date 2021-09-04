from odoo import api, fields, models


class HrReferralApplication(models.Model):
    _name = "hr.referral.application"
    _description = "Hr Referral Application"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email", default="xyz@gmail.com")
    referral_name = fields.Many2one("hr.employee", string="Referral Name")
    degree = fields.Many2one("hr.recruitment.degree", string="Degree")
    department = fields.Many2one("hr.job", string="Department")
    expected_salary = fields.Integer(string="Salary")
    summary = fields.Text(string="Summary")
    expected_joining_date = fields.Date(string="Expected Joining Date")
    state = fields.Selection(
        [("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
        default="draft",
        string="Status",
    )

    def action_approved(self):
        self.state = "approved"

    # def action_createapp(self):
    #     pass

    def action_cancel(self):
        self.state = "cancel"

    def action_draft(self):
        self.state = "draft"
