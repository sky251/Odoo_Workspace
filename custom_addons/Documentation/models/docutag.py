from odoo import api, fields, models


class DocumentTag(models.Model):
    _name = "docu.tag"
    _description = "This is documentation tag"


    name = fields.Char(string="Document tag")
    color = fields.Integer()
    active = fields.Boolean(string="Active")


