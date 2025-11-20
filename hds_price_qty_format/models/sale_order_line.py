# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Redefinir campos con precisión de 2 decimales
    product_uom_qty = fields.Float(
        string="Quantity",
        digits=(16, 2),  # Cambiar a 2 decimales
        default=1.0,
        required=True,
    )

    price_unit = fields.Float(
        string="Unit Price",
        digits=(16, 2),  # Cambiar a 2 decimales
        required=True,
        default=0.0,
    )

