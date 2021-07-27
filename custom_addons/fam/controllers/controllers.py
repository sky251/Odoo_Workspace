# -*- coding: utf-8 -*-
# from odoo import http


# class Fam(http.Controller):
#     @http.route('/fam/fam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fam/fam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fam.listing', {
#             'root': '/fam/fam',
#             'objects': http.request.env['fam.fam'].search([]),
#         })

#     @http.route('/fam/fam/objects/<model("fam.fam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fam.object', {
#             'object': obj
#         })
