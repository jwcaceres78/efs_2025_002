from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state_sale = fields.Char(string='Estado de Venta')
    customer_category = fields.Selection([
        ('premium', 'Premium'),
        ('wholesale', 'Mayorista'),
        ('retail', 'Minorista')
    ], string='Categoría de Cliente', default='retail', required=True)
    
