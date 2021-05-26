# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC <info@planetatic.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class PickingType(models.Model):
    _inherit = 'stock.picking.type'
    scheduler_not_assign = fields.Boolean(string="Not assign by scheduler")
