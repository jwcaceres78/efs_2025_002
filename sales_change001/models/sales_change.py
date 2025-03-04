from odoo import models, fields, api


class SalesChange(models.Model):
    _name = 'change'
    _description = 'modelo para registra los cambios de las ventas'

    name = fields.Char()
    value = fields.Float()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    long_description = fields.Html()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

