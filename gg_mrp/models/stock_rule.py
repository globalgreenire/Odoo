################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2019 N-Development (<https://n-development.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_mo_vals(
            self, product_id, product_qty, product_uom,
            location_id, name, origin, company_id, values, bom):
        vals = super(StockRule, self)._prepare_mo_vals(
            product_id, product_qty, product_uom,
            location_id, name, origin, company_id, values, bom)
        order = self.env['sale.order'].search([('name', '=', origin)],
                                                 limit=1)
        vals['gg_origin_customer'] = order and order.partner_id.display_name or ''
        return vals
