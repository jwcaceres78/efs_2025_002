# # -*- coding: utf-8 -*-
# # from odoo import http


# class SalesChange001(http.Controller):
#     @http.route('/sales_change001/sales_change001', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_change001/sales_change001/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_change001.listing', {
#             'root': '/sales_change001/sales_change001',
#             'objects': http.request.env['sales_change'].search([]),
#         })

#     @http.route('/sales_change001/sales_change001/objects/<model("sales_change"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_change001.object', {
#             'object': obj
#         })

