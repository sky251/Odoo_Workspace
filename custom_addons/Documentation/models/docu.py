from odoo import api, fields, models


class Documentation(models.Model):
    _name = "docu.item"
    _description = "This is documentation task"

    name = fields.Char(string="Document name")
    description_sort = fields.Text(string="Sort description")
    description_long = fields.Html(string="Long description")
    video_url = fields.Char(string="Video url")
    google_document_url = fields.Char(string="Google doc url")

    @api.model
    def _selection_languages(self):
        return self.env['res.lang'].get_installed()


    lang = fields.Selection(_selection_languages, string='Template Preview Language')
