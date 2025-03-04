# -*- coding: utf-8 -*-
{
    'name': "delivery de compras online",

    'summary': "Módulo para gestionar la entrega de compras online",

    'description': """
    Módulo para gestionar la entrega de compras online
    """,

    'author': "EFS",
    'website': "https://www.escuelafullstack.com",

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
        'views/res_partner.xml',
        'views/transporter.xml',
        'views/sale_oder.xml',
    ],
    # only loaded in demonstration mode
}

