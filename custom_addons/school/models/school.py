from odoo import models, fields


class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'School Information'
    _rec_name = "email"

    name = fields.Char(string='School name', help='Write a school name', required=True, index=True, )
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    parking = fields.Boolean(string='Parking')
    result = fields.Float(string='Result')
    fees = fields.Integer(string='Fees')
    school_address = fields.Text(string='School address')
    establish_date = fields.Date(string='Establish date')
    open_date = fields.Datetime(string='open date')
    courses = fields.Selection([
        ('computer', 'Computer'),
        ('electrical', 'Electrical')],
        string='Course selection')
    documents = fields.Binary(string='Documents')
    docu_name = fields.Char(string='Documents name')
    image = fields.Binary(attachment=True, store=True)
    image_name = fields.Char(string="Image Name", invisible="1")
    school_desc = fields.Html(string='School description')


