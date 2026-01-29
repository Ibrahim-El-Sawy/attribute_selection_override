# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class attribute_selection_override(models.Model):
#     _name = 'attribute_selection_override.attribute_selection_override'
#     _description = 'attribute_selection_override.attribute_selection_override'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

