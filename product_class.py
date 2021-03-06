# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class ProductClass(osv.Model):
    _name = 'product.class'
    _description = 'Class for the product (eg. subproduct, packaging, ...)'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=64, translate=True),
        'code': fields.char('Code', size=64, translate=False),
        'description': fields.text('Description', translate=True),
    }

class ProductProduct(osv.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    _columns = {
        'class_id': fields.many2one('product.class', 'Product Class',
                                    help="Add a class to product and use it for product filtering",
                                    required=False),
    }
