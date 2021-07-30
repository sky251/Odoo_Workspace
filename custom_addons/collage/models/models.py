# -*- coding: utf-8 -*-

from odoo import models, fields, api


class collage(models.Model):
    _name = 'collage.profile'
    _description = 'collage Management'

    name = fields.Char()
    value = fields.Integer()

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
