# Copyright 2022 Ecosoft Co., Ltd (http://ecosoft.co.th/).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountReconciliation(models.AbstractModel):
    _inherit = "account.reconciliation.widget"

    @api.model
    def _prepare_move_lines(
        self, move_lines, target_currency=False, target_date=False, recs_count=0
    ):
        ret = super()._prepare_move_lines(
            move_lines, target_currency, target_date, recs_count
        )
        AccountMoveLine = self.env["account.move.line"]
        for line in ret:
            move_line = AccountMoveLine.browse(line["id"])
            line["check_number"] = move_line.check_number or ""
        return ret

    @api.model
    def _get_statement_line(self, st_line):
        data = super()._get_statement_line(st_line)
        data["check_number"] = st_line.check_number or ""
        return data
