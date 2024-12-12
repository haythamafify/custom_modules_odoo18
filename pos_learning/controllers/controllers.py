# -*- coding: utf-8 -*-
# from odoo import http


# class PosLearning(http.Controller):
#     @http.route('/pos_learning/pos_learning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_learning/pos_learning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_learning.listing', {
#             'root': '/pos_learning/pos_learning',
#             'objects': http.request.env['pos_learning.pos_learning'].search([]),
#         })

#     @http.route('/pos_learning/pos_learning/objects/<model("pos_learning.pos_learning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_learning.object', {
#             'object': obj
#         })

