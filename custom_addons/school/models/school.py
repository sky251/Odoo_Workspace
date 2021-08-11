from odoo import api, models, fields


class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'School Information'
    # _rec_name = "name"

    @api.depends("courses")
    def _compute_course_wise_salary(self):
        for cor in self:
            if cor.courses == "computer":
                cor.salary = 28000
            elif cor.courses == "electrical":
                cor.salary = 30000
            elif cor.courses == "automobile":
                cor.salary = 32000
            elif cor.courses == "civil":
                cor.salary = 27000
            else:
                cor.salary = 10000

    name = fields.Char(string='School name', help='Write a school name', index=True, )
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    parking = fields.Boolean(string='Parking')
    result = fields.Float(string='Result')
    fees = fields.Integer(string='Fees')
    salary = fields.Integer(compute="_compute_course_wise_salary", string='Salary', readonly=True,store=True)
    school_address = fields.Text(string='School address')
    establish_date = fields.Date(string='Establish date')
    open_date = fields.Datetime(string='open date')
    courses = fields.Selection([
        ('computer', 'Computer'),
        ('automobile', 'Auto Mobile'),
        ('civil', 'Civil'),
        ('mechanical', 'Mechanical'),
        ('electrical', 'Electrical')],
        string='Course selection')
    documents = fields.Binary(string='Documents')
    docu_name = fields.Char(string='Documents name')
    image = fields.Binary(attachment=True, store=True)
    image_name = fields.Char(string='Image Name', invisible='1')
    school_desc = fields.Html(string='School description')
    student_data_ids = fields.One2many('student.profile', 'school_select_id', string='Student data')

