from odoo import models, fields

class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Student Information'

    student_name = fields.Char(string='Student name')
    student_email = fields.Char(string='Email')
    student_phone = fields.Char(string='Phone')
    student_result = fields.Float(string='Result')
    student_img = fields.Image(string=' Upload student image', max_width=100, max_height=100)
    school_select = fields.Many2one("school.profile", string="Select School")
