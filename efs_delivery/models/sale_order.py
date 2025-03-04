from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    transporter_id = fields.Many2one('transporter', string='Transportista')
    delivery_state = fields.Selection([
        ('warehouse', 'En Almacén'),
        ('route', 'En Ruta'),
        ('delivered', 'Entregado')
    ], string='Estado de Envío', default='warehouse')
