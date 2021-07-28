from odoo import models,fields

class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string='School name')
    email = fields.Char(string='Email')
    phonegf = fields.Char()