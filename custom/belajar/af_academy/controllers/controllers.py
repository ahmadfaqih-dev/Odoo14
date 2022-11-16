# -*- coding: utf-8 -*-
# from odoo import http


# class AfAcademy(http.Controller):
#     @http.route('/af_academy/af_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/af_academy/af_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('af_academy.listing', {
#             'root': '/af_academy/af_academy',
#             'objects': http.request.env['af_academy.af_academy'].search([]),
#         })

#     @http.route('/af_academy/af_academy/objects/<model("af_academy.af_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('af_academy.object', {
#             'object': obj
#         })
