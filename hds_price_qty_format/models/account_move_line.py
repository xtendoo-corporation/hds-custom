# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # Redefinir campos con precisión de 2 decimales
    quantity = fields.Float(
        string='Quantity',
        default=1.0,
        digits=(16, 2),  # Cambiar a 2 decimales
        help="The optional quantity expressed by this line, eg: number of product sold. "
             "The quantity is not a legal requirement but is very useful for some reports."
    )

    price_unit = fields.Float(
        string='Unit Price',
        digits=(16, 2),  # Cambiar a 2 decimales
    )

