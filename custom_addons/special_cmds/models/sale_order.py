from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_partner_ids = fields.Many2many('res.partner', 'partner_rel', '', 'partner_id', string="Partner")

    def mail_wizard_button(self):
        print("\n\n\n\n\n Mail Wizard Button")
        # self.custom_partner_ids= [(6,0,[14,23,33])] # Delet existing record and create new record
        # self.custom_partner_ids = [(1, 44, {'phone': '8460232337'})] # Update record from database,only if record already in db.
        # self.custom_partner_ids= [(2,14)] # Delete record from database

        # self.custom_partner_ids = [(4,27)]
        # self.custom_partner_ids = [(5,)]
        # [0,0,{}]
        # range_list=[]
        # for i in range(0,2):
        #     cust_dict={'name':i}
        #     range_list.append(cust_dict)
        # for val in range_list:
        #     print ("iiiiiiiiii",val)
        #     self.partner_cust_ids = [(0,0,val)]

        # self.ensure_one()
        # template_id = self._find_mail_template()
        # # template_custom_id = self.env.ref('module_name.template_id')
        # lang = self.env.context.get('lang')
        # template = self.env['mail.template'].browse(template_id)
        # if template.lang:
        #     lang = template._render_lang(self.ids)[self.id]
        # ctx = {
        #     'default_model': 'sale.order',
        #     'default_res_id': self.ids[0],
        #     'default_partner_ids':[(6,0,[14,23,33])],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'custom_layout': "mail.mail_notification_paynow",
        #     'proforma': self.env.context.get('proforma', False),
        #     'force_email': True,
        #     'model_description': self.with_context(lang=lang).type_name,
        # }
        # ctx= {
        #     'default_phone':'84555555532',
        #     'my_name':'arti'
        # }
        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'res.partner',
        #     'views': [(False, 'form')],
        #     'view_id': False,
        #     'target': 'new',
        #     'context': ctx,
        # }
