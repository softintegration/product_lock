# -*- coding: utf-8 -*- 


{
    'name': 'Product lock',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.2',
    'category': 'Product',
    'demo': [],
    'depends': ['product','model_lock'],
    'data': [
        'security/product_lock_security.xml',
        'views/product_views.xml',

    ],
    'license': 'LGPL-3',
}
