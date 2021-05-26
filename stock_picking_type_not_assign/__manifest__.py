# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC <info@planetatic.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Stock Picking Type Not Assign',
    "summary": "Permits to set stock picking types to not assign by scheduler",
    'version': '12.0.1.0.1',
    "development_status": "Production/Stable",
    "category": "Stock",
    'author': "PlanetaTIC,Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/stock-logistics-workflow',
    'depends': [
        'stock',
    ],
    'demo': [],
    'data': [
        'views/stock_picking.xml',
    ],
    'installable': True,
    'auto_install': False,
}
