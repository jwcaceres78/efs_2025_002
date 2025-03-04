from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_category = fields.Selection([
        ('premium', 'Premium'),
        ('wholesale', 'Mayorista'),
        ('retail', 'Minorista')
    ], string='Categoría de Cliente', default='retail', required=True)
