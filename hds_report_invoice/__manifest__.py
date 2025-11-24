{
    'name': 'HDS Report Invoice',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Swap customer address with invoice number position in invoice report',
    'description': """
        This module swaps the position of:
        - Customer address: moved to the left
        - Invoice number: moved to the right

        This is useful when using envelopes with transparent windows on the right side.
    """,
    'author': 'Ivan Parrado',
    'website': 'https://www.xtendoo.es',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/report_invoice_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

