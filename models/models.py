# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_hm_core(models.Model):
#     _name = 'smart_hm_core.smart_hm_core'
#     _description = 'smart_hm_core.smart_hm_core'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
