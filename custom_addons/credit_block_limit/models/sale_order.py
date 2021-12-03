from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self,vals):
        print("\n\n\n\n\n\n Before Valsss",vals)
        rtn = super(SaleOrder, self).create(vals)
        print("\n\n\n\n\n\n After Valsss",vals)
        # print("rtnnn\n\n\n\n\n",rtn)

        credit_score,blocking_score = rtn.partner_id.credit_limit_score,rtn.partner_id.blocking_limit_score
        email_to = rtn.env['ir.config_parameter'].get_param("credit_block_limit.email_to")
        print("\n\n\n\n email_to",email_to)
        if credit_score :
            total_amount = 0
            # total_amount += rtn.amount_total
            for amount in rtn.env['sale.order'].search([('partner_id', '=', rtn.partner_id.id), ('state', 'in', ['draft', 'sent'])]):
                total_amount = total_amount + amount.amount_total
            if credit_score < total_amount:
                if email_to:
                    template = rtn.env.ref('credit_block_limit.partner_mail_template_view')
                    template.send_mail(rtn.id, email_values={"email_to":email_to})
                    raise ValidationError('Your Sale Order Credit Limit has been Exceeded.')


        if blocking_score:
            total_amount = 0
            total_amount =total_amount + rtn.amount_total
            for amount in rtn.env['sale.order'].search(
                    [('partner_id', '=', rtn.partner_id.id), ('state', 'in', ['draft', 'sent'])]):
                total_amount = total_amount + amount.amount_total
                print(amount)
            if total_amount > blocking_score:
                if email_to:
                    template = rtn.env.ref('credit_block_limit.partner_mail_template_view')
                    template.send_mail(rtn.id, email_values={"email_to":email_to})
                    raise ValidationError('You cannot create SO as the Block Limit has been Exceeded')

        return rtn

