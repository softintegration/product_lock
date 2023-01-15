# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'model.lock.class']



