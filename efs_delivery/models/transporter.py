from odoo import models, fields

class Transporter(models.Model):
    _name = 'transporter'
    _description = 'Transportista para entregas'

    name = fields.Char(string='Nombre', required=True)
    identification = fields.Char(string='Identificación', required=True)
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    active = fields.Boolean(string='Activo', default=True)
    
    vehicle_type = fields.Selection([
        ('bike', 'Bicicleta'),
        ('motorcycle', 'Motocicleta'),
        ('car', 'Automóvil'),
        ('van', 'Furgoneta')
    ], string='Tipo de Vehículo', required=True)
    
    license_plate = fields.Char(string='Matrícula del Vehículo')
    delivery_zone = fields.Char(string='Zona de Reparto')
    
    available = fields.Boolean(string='Disponible', default=True)
    current_latitude = fields.Float(string='Latitud Actual')
    current_longitude = fields.Float(string='Longitud Actual')
    
    delivery_count = fields.Integer(string='Entregas Realizadas', default=0)
    rating = fields.Float(string='Calificación Promedio', default=0.0)
