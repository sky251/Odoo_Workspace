from odoo import models, fields


class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Student Information'

    def _compute_total_calcu(self):
        for rec in self:
            if rec.is_parking == True:
                rec.calculate = 50
            elif rec.is_parking == False:
                rec.calculate = 100

    name = fields.Char(string='Student name')
    student_email = fields.Char(string='Email')
    student_phone = fields.Char(string='Phone')
    student_result = fields.Float(string='Result')
    student_img = fields.Image(string=' Upload student image', max_width=100, max_height=100)
    school_select_id = fields.Many2one("school.profile", string="Select School")
    user_signature = fields.Binary(string='Signature')
    is_parking = fields.Boolean(related="school_select_id.parking", string="Is parking", store=True)
    calculate = fields.Integer(compute="_compute_total_calcu", string="Calculate")
    state = fields.Selection([('one','One'),('two','Two'),('three','Three')], default='one', string="Status")

    def action_confirm(self):
        self.state = 'two'

    def action_done(self):
        self.state = "three"