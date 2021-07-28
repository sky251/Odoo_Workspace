from odoo import models,fields

class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string='school name')
    email = fields.Char(string='Email')
    phone = fields.Char('Phone')