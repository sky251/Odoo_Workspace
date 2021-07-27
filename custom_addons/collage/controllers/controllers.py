# -*- coding: utf-8 -*-
# from odoo import http


# class Collage(http.Controller):
#     @http.route('/collage/collage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/collage/collage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('collage.listing', {
#             'root': '/collage/collage',
#             'objects': http.request.env['collage.collage'].search([]),
#         })

#     @http.route('/collage/collage/objects/<model("collage.collage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('collage.object', {
#             'object': obj
#         })
