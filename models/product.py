# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Product(models.Model):
    _name = 'product.product'
    _inherit = ['product.product', 'model.lock.class']



