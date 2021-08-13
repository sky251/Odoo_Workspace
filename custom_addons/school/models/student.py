from odoo import api, fields, models


class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Student Information'
    @api.depends("is_parking")
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
    state = fields.Selection(
        [('draft', 'draft'), ('confirm', 'confirm'), ('done', 'done'), ('cancel', 'cancel')],
        default='draft', string="Status")

    @api.model_create_multi
    def create(self, vals):
        rtn = super(StudentProfile, self).create(vals)
        return rtn

    def write(self, vals):
        rtn = super(StudentProfile, self).write(vals)
        return rtn

    def unlink(self):
        rtn = super(StudentProfile, self).unlink()
        print("\n\n\nrtn\n\n\n", rtn)
        return rtn

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_reset(self):
        self.state = 'draft'

    def clear_record_data(self):
        self.write({
            'name': None,
            'student_email': None,
            'student_phone': None,
            'student_result': None,
            'student_img': None,
            'user_signature': None,
            'is_parking': None,
            'calculate': None,
        })
