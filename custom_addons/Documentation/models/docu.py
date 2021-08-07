from odoo import models, fields

class Documentation(models.Model):
    _name = "docu.item"
    _description = "This is documentation task"

    name = fields.Char(string = "Document name")
    description_sort = fields.Char(string = "Sort description")
    description_long = fields.Char(string = "Long description")
    video_url = fields.Char(string="Video url")
    google_document_url = fields.Char(string="Google doc url")
