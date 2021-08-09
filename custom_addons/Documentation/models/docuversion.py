from odoo import api, fields, models


class DocumentTag(models.Model):
    _name = "docu.version"
    _description = "This is documentation tag"
    _rec_name = "ver_no"


    ver_no = fields.Integer(string='Version no')
    active = fields.Boolean(string="Active")


