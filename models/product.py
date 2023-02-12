# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Product(models.Model):
    _name = 'product.product'
    _inherit = ['product.product', 'model.lock.class']


    @api.model_create_multi
    def create(self, vals_list):
        recs = super(Product, self).create(vals_list)
        recs.with_context(force_update=True)._action_lock()
        return recs


