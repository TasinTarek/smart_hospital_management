# -*- coding: utf-8 -*-
# from odoo import http


# class SmartHmCore(http.Controller):
#     @http.route('/smart_hm_core/smart_hm_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_hm_core/smart_hm_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_hm_core.listing', {
#             'root': '/smart_hm_core/smart_hm_core',
#             'objects': http.request.env['smart_hm_core.smart_hm_core'].search([]),
#         })

#     @http.route('/smart_hm_core/smart_hm_core/objects/<model("smart_hm_core.smart_hm_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_hm_core.object', {
#             'object': obj
#         })
