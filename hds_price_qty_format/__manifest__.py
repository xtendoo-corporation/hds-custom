{
    'name': 'HDS Price and Quantity Format',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Adjust decimal precision for quantities and unit prices',
    'description': """
        This module adjusts the decimal precision for:
        - Quantities: from 3 to 2 decimals
        - Unit Prices: from 5 to 2 decimals
    """,
    'author': 'Ivan Parrado',
    'website': 'https://www.xtendoo.es',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'sale',
        'account',
    ],
    'data': [],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}

