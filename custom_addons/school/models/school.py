from odoo import models,fields

class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'School Information'

    school_name = fields.Char(string='School name',help='Write a school name',required = True,trim = False,index=True,)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')