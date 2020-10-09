# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    pos_payment_ref = fields.Boolean('Record Payment Ref', default=False)


class POSPayment(models.Model):
    _inherit = 'pos.payment'

    note = fields.Char('Payment Reference')
    payment_ref = fields.Char('Payment Reference')

    @api.model
    def create(self, vals):
        res = super(POSPayment, self).create(vals)
        return res

class POSOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def _payment_fields(self, order, ui_paymentline):
        """Filters out excess fields"""
        res = super(POSOrder, self)._payment_fields(order, ui_paymentline)
        res.update({
            'payment_ref': ui_paymentline.get('payment_ref'),
        })
        return res
