from odoo import models, fields

class Documentation(models.Model):
    _name = "documentation"
    _description = "This is documentation task"

    dname = fields.Char(string = "Document name")
    description_sort = fields.Char(string = "Sort desc")
    description_long = fields.Char(string = "Long desc")
    video_url = fields.Char(string="Video url")
    ggl_doc_url = fields.Binary(string="")
