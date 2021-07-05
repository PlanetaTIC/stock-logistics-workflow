# Copyright 2021 PlanetaTIC <info@planetatic.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError 


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def force_internal(self):
        product_obj = self.env['product.product']
        move_obj = self.env['stock.move']
        self.ensure_one()

        if self.picking_type_id.code != 'internal':
            raise UserError(_('Picking %s is not an internal picking.') % (
                self.picking.name))

        if self.state == 'confirmed':
            # check available:
            self.action_assign()
        if self.state == 'assigned':
            self.button_validate()
            return True

        reserve_products = {}
        for move in self.move_lines:
            product = product_obj.with_context(
                location=self.location_id.id).browse(move.product_id.id)
            # verify there is enough stock in origin location:
            if move.product_qty > product.qty_available:
                raise UserError(_(
                    'Not enough quantities of %s to move from location %s') % (
                        move.product_id.default_code, self.location_id.name))
            reserve_products[product.id] = {
                'requested_qty': move.product_qty,
                'location_qty': product.qty_available - product.outgoing_qty,
                'pending_qty': move.product_qty - (
                    product.qty_available - product.outgoing_qty),
                'moves_to_treat': self.env['stock.move'],
            }

        for product_id, reserve in reserve_products.items():
            if reserve['pending_qty'] <= 0:
                continue
            candidate_moves = move_obj.search([
                ('location_id', '=', self.location_id.id),
                ('product_id', '=', product_id),
                ('state', '=', 'assigned'),
            ])
            for candidate_move in candidate_moves:
                reserve['pending_qty'] -= candidate_move.reserved_availability
                reserve['moves_to_treat'] |= candidate_move
                if reserve['pending_qty'] <= 0:
                    break

        # Cancel reserved stock, to validate our internal picking:
        moves_to_reserve = self.env['stock.move']
        for product_id, reserve in reserve_products.items():
            for move in reserve['moves_to_treat']:
                move.do_unreserve()
                moves_to_reserve |= move

        # validate picking
        self.action_assign()
        for move in self.move_lines.filtered(
                lambda m: m.state not in ['done', 'cancel']):
            for move_line in move.move_line_ids:
                move_line.qty_done = move_line.product_uom_qty
        self.action_done()

        # chack availability of previous unreserved lines:
        moves_to_reserve._action_assign()

        return True
