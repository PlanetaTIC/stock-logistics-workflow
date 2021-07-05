# Copyright 2021 PlanetaTIC <info@planetatic.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Stock Picking Force Internal",
    "summary":
        "Given a internal stock picking, "
        "you can check available and validate all at once,"
        " breaking resesrved stock if necessary",
    "version": "12.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Stock",
    "website": "https://www.planetatic.com/",
    "author": "PlanetaTIC",
    "maintainers": ["PlanetaTIC"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "stock_picking_unreserve_line",
    ],
    "data": [
        'views/stock_picking_views.xml',
    ],
}
