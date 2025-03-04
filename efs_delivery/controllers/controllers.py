# -*- coding: utf-8 -*-
# from odoo import http


# class EfsDelivery(http.Controller):
#     @http.route('/efs_delivery/efs_delivery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/efs_delivery/efs_delivery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('efs_delivery.listing', {
#             'root': '/efs_delivery/efs_delivery',
#             'objects': http.request.env['efs_delivery.efs_delivery'].search([]),
#         })

#     @http.route('/efs_delivery/efs_delivery/objects/<model("efs_delivery.efs_delivery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('efs_delivery.object', {
#             'object': obj
#         })

