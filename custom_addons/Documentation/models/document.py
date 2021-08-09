from odoo import api, fields, models


class Documentation(models.Model):
    _name = "docu.item"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This is documentation task"

    @api.model
    def _selection_languages(self):
        return self.env['res.lang'].get_installed()

    name = fields.Char(string="Document name", required=True)
    description_sort = fields.Text(string="Sort description", required=True)
    description_long = fields.Html(string="Long description")
    video_url = fields.Char(string="Video url")
    google_document_url = fields.Char(string="Google doc url")
    lang = fields.Selection(_selection_languages, string='Template Language')
    tag_ids = fields.Many2many('docu.tag', string="Tag")
    active = fields.Boolean(string="Active")
    doc_version_ids = fields.Many2one('docu.version', string="Doc version", required=True)
    language = fields.Selection(
        [
            ("py", "PYTHON"),
            ("pp", "PHP"),
            ("nt", ".NET"),
            ("jv", "JAVA"),
            ("as", "AWS"),
        ],
        string="Task Language",
    )
