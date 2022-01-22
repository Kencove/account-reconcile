# Copyright 2022 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class MassReconcileAdvanced(models.AbstractModel):
    _inherit = "mass.reconcile.advanced"

    def _selection_columns(self):
        aml_cols = super(MassReconcileAdvanced, self)._selection_columns()
        aml_cols.append("account_move_line.stock_valuation_adjustment_line_id")
        aml_cols.append("account_move_line.stock_landed_cost_id")
        return aml_cols