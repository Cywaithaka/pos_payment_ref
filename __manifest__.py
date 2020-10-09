# -*- coding: utf-8 -*-
{
    'name': 'POS Payment Ref',
    'version': '12.0.1.0.0',
    'summary': """Allow POS cashier to capture of payment reference / code""",
    'category': 'Point of Sale',
    'license': 'LGPL-3',
    'author': "Explore Data Systems",
    'website': "http://exploredatasystems.com/",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_ref.xml',
        'views/views.xml',
    ],
    'images': [],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/*.xml'],
}
