# -*- coding: utf-8 -*-
# from odoo import http


# class SalesChange002(http.Controller):
#     @http.route('/sales_change002/sales_change002', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_change002/sales_change002/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_change002.listing', {
#             'root': '/sales_change002/sales_change002',
#             'objects': http.request.env['sales_change002.sales_change002'].search([]),
#         })

#     @http.route('/sales_change002/sales_change002/objects/<model("sales_change002.sales_change002"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_change002.object', {
#             'object': obj
#         })

