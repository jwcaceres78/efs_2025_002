# -*- coding: utf-8 -*-
{
    'name': "agregar fecha de pago a las ventas",

    'summary': "Modulo para registrar la fecha de pago de las ventas",

    'description': """
Modulo para registrar la fecha de pago de las ventas
    """,

    'author': "Jorge W.",
    'website': "https://www.gemastic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

