# HDS Report Invoice

## Description

This module swaps the position of the customer address and invoice number in the invoice report for HDS Metalica.

### Features

- **Customer address**: Moved to the left side
- **Invoice number**: Stays on the right side (in the external layout header)

This is useful when using envelopes with transparent windows on the right side, as the invoice number will be visible through the window while the customer address is on the left.

### Installation

1. Install the module from the Odoo Apps menu
2. The change will be automatically applied to all invoice reports

### Configuration

No configuration needed. The layout is automatically applied to invoice reports using the Bubble design.

### Usage

After installing the module, when you print or preview an invoice:
- The customer address will appear on the left side
- The invoice number will appear on the right side (in the header)

This works with all invoice types:
- Customer Invoices
- Credit Notes
- Vendor Bills
- Vendor Credit Notes

## Author

Ivan Parrado - Xtendoo

## License

LGPL-3

