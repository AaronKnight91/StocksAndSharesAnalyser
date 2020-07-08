import sqlite3

class CompanyDatabase:

    def __init__(self, db, table):
        self._table = table.replace(" ", "")
        self._conn = sqlite3.connect(db)
        self._cur = self._conn.cursor()
        self._cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, date TEXT, pe_ratio REAL, ps_ratio REAL, cash_flow REAL, free_cash_flow REAL, pb_ratio REAL, tangibe_pb_ratio REAL, gross_margin_ttm REAL, gross_margin_5ya REAL, operating_margin_ttm REAL, operating_margin_5ya REAL, pretax_margin_ttm REAL, pretax_margin_5ya REAL, net_profit_margin_ttm REAL, net_profit_margin_5ya REAL, revenue_per_share REAL, basic_eps REAL, diluted_eps REAL, book_value_per_share REAL, tangible_book_value_per_share REAL, cash_per_share REAL, cash_flow_per_share REAL, return_on_equity_ttm REAL, return_on_equity_5ya REAL, return_on_assets_ttm REAL, return_on_assets_5ya REAL, return_on_investment_ttm REAL, return_on_investment_5ya REAL, eps_mrq_vs_mrq_1yr_ago REAL, eps_ttm_vs_ttm_1yr_ago REAL, eps_growth_5ya REAL, sale_mrq_vs_qtr_1ya_ago REAL, self_ttm_vs_ttm_1ya_ago REAL, sale_mrq_vs_qtr_1ya_ago REAL, sale_ttm_vs_ttm_1ya_ago REAL, sales_growth_5ya REAL, capital_spending_growth_5ya REAL, quick_ratio REAL, current_ratio REAL, lt_debt_to_equity REAL, total_debt_to_equity REAL, asset_turnover REAL, inventory_turnover REAL, revenue_per_employee REAL, net_income_per_employee REAL, receivable_turnover REAL, dividend_yield REAL, dividend_yield_5ya REAL, dividend_growth_rate REAL, payout_ratio REAL)" % self._table)
        self._conn.commit()

    def insert(self, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("INSERT INTO %s VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)" % self._table,
                          (date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio))
        self._conn.commit()

    def view(self):
        self._cur.execute("SELECT * FROM %s" % self._table)
        rows = self._cur.fetchall()
        return rows

    def search(self, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("SELECT * FROM %s WHERE pe_ratio=? OR ps_ratio=? OR cash_flow=? OR pb_ratio=? OR dividend_yield OR payout_ratio=?" % self._table, (pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio))
        rows = self._cur.fetchall()
        return rows

    def update(self, id, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("UPDATE %s SET pe_ratio=?, ps_ratio=?, cash_flow=?, pb_ratio=?, dividend_yield=?, payout_ratio=? WHERE id=?" % self._table,
                         (pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio,id))
        self._conn.commit()

    def remove_duplicate_rows(self):
        self._cur.execute("DELETE From %s WHERE id not in (SELECT max(id) from %s group by date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio)" % (self._table, self._table))
        self._conn.commit()

    def delete(self, id):
        self._cur.execute("DELETE FROM %s WHERE id=?" % self._table,(id,))
        self._conn.commit()

    def __del__(self):
        self._conn.close()
