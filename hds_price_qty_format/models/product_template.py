# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Redefinir el campo list_price con 2 decimales en lugar de los predeterminados
    list_price = fields.Float(
        'Sales Price',
        default=1.0,
        digits=(16, 2),  # Cambiar a 2 decimales
        help="Price at which the product is sold to customers.",
    )

    standard_price = fields.Float(
        'Cost',
        compute='_compute_standard_price',
        inverse='_set_standard_price',
        search='_search_standard_price',
        digits=(16, 2),  # Cambiar a 2 decimales
        groups="base.group_user",
        help="""In Standard Price & AVCO: value of the product (automatically computed in AVCO).
        In FIFO: value of the last unit that left the stock (automatically computed).
        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
        Used to compute margins on sale orders."""
    )

