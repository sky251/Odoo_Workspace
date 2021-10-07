from odoo import api, fields, models


class TeamMember(models.Model):
    _name = "team.member"
    _description = "Team member"

    partner_id = fields.Many2one("res.partner", string="Partner")
    name = fields.Char(related="member_id.name", string="Name")
    email = fields.Char(related="member_id.email", string="Name")
    phone = fields.Char(related="member_id.phone", string="Name")
    member_id = fields.Many2one("res.partner", string="Member")

class ResPartner(models.Model):
    _inherit = "res.partner"

    team_member_ids = fields.One2many(
        "team.member", "partner_id", string="Team member id"
    )

    boolean_tl = fields.Boolean(string="TL")
