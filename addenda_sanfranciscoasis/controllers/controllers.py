# -*- coding: utf-8 -*-
from odoo import http

# class AddendaSanfranciscoasis(http.Controller):
#     @http.route('/addenda_sanfranciscoasis/addenda_sanfranciscoasis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_sanfranciscoasis/addenda_sanfranciscoasis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_sanfranciscoasis.listing', {
#             'root': '/addenda_sanfranciscoasis/addenda_sanfranciscoasis',
#             'objects': http.request.env['addenda_sanfranciscoasis.addenda_sanfranciscoasis'].search([]),
#         })

#     @http.route('/addenda_sanfranciscoasis/addenda_sanfranciscoasis/objects/<model("addenda_sanfranciscoasis.addenda_sanfranciscoasis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_sanfranciscoasis.object', {
#             'object': obj
#         })