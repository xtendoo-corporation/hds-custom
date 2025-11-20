# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Hook ejecutado después de la instalación del módulo."""
    _logger.info("Actualizando precisiones decimales...")

    # Actualizar precisión de cantidades (Product Unit of Measure)
    precision_uom = env['decimal.precision'].search([
        ('name', '=', 'Product Unit of Measure')
    ], limit=1)
    if precision_uom:
        precision_uom.write({'digits': 2})
        _logger.info("Precisión de 'Product Unit of Measure' actualizada a 2 decimales")

    # Actualizar precisión de precios (Product Price)
    precision_price = env['decimal.precision'].search([
        ('name', '=', 'Product Price')
    ], limit=1)
    if precision_price:
        precision_price.write({'digits': 2})
        _logger.info("Precisión de 'Product Price' actualizada a 2 decimales")

    # Actualizar precisión de descuentos (Discount)
    precision_discount = env['decimal.precision'].search([
        ('name', '=', 'Discount')
    ], limit=1)
    if precision_discount:
        precision_discount.write({'digits': 2})
        _logger.info("Precisión de 'Discount' actualizada a 2 decimales")

    _logger.info("Precisiones decimales actualizadas exitosamente")

