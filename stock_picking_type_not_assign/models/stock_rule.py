# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC <info@planetatic.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def _get_moves_to_assign_domain(self, company_id):
        domain = super(ProcurementGroup, self)._get_moves_to_assign_domain(
            company_id)
        domain = expression.AND(
            [domain, [('picking_type_id.scheduler_not_assign', '=', False)]])
        return domain
