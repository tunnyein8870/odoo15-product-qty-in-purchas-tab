# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseProduct(http.Controller):
#     @http.route('/purchase_product/purchase_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_product/purchase_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_product.listing', {
#             'root': '/purchase_product/purchase_product',
#             'objects': http.request.env['purchase_product.purchase_product'].search([]),
#         })

#     @http.route('/purchase_product/purchase_product/objects/<model("purchase_product.purchase_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_product.object', {
#             'object': obj
#         })
