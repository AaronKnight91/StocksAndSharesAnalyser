import sqlite3

class CompanyDatabase:

    def __init__(self, today, db, table):
        self._today = today
        self._table = table.replace(" ", "")

        self._conn = sqlite3.connect(db)
        self._cur = self._conn.cursor()
        self._cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, date TEXT, pe_ratio REAL, ps_ratio REAL, cash_flow REAL, free_cash_flow REAL, pb_ratio REAL, tangible_pb_ratio REAL, gross_margin_ttm REAL, gross_margin_5ya REAL, operating_margin_ttm REAL, operating_margin_5ya REAL, pretax_margin_ttm REAL, pretax_margin_5ya REAL, net_profit_margin_ttm REAL, net_profit_margin_5ya REAL, revenue_per_share REAL, basic_eps REAL, diluted_eps REAL, book_value_per_share REAL, tangible_book_value_per_share REAL, cash_per_share REAL, cash_flow_per_share REAL, return_on_equity_ttm REAL, return_on_equity_5ya REAL, return_on_assets_ttm REAL, return_on_assets_5ya REAL, return_on_investment_ttm REAL, return_on_investment_5ya REAL, eps_mrq_vs_mrq_1yr_ago REAL, eps_ttm_vs_ttm_1yr_ago REAL, eps_growth_5ya REAL, sale_mrq_vs_qtr_1ya_ago REAL, sale_ttm_vs_ttm_1ya_ago REAL, sales_growth_5ya REAL, capital_spending_growth_5ya REAL, quick_ratio REAL, current_ratio REAL, lt_debt_to_equity REAL, total_debt_to_equity REAL, asset_turnover REAL, inventory_turnover REAL, revenue_per_employee REAL, net_income_per_employee REAL, receivable_turnover REAL, dividend_yield REAL, dividend_yield_5ya REAL, dividend_growth_rate REAL, payout_ratio REAL)" % self._table)##_name)
        self._conn.commit()

    def insert(self, pe_ratio=None, ps_ratio=None, cash_flow=None, free_cash_flow=None, pb_ratio=None, tangible_pb_ratio=None,
               gross_margin_ttm=None, gross_margin_5ya=None, operating_margin_ttm=None, operating_margin_5ya=None, pretax_margin_ttm=None,
               pretax_margin_5ya=None, net_profit_margin_ttm=None, net_profit_margin_5ya=None, revenue_per_share=None, basic_eps=None,
               diluted_eps=None, book_value_per_share=None, tangible_book_value_per_share=None, cash_per_share=None, cash_flow_per_share=None,
               return_on_equity_ttm=None, return_on_equity_5ya=None, return_on_assets_ttm=None, return_on_assets_5ya=None,
               return_on_investment_ttm=None, return_on_investment_5ya=None, eps_mrq_vs_mrq_1yr_ago=None, eps_ttm_vs_ttm_1yr_ago=None,
               eps_growth_5ya=None, sale_mrq_vs_qtr_1ya_ago=None, sale_ttm_vs_ttm_1ya_ago=None, sales_growth_5ya=None,
               capital_spending_growth_5ya=None, quick_ratio=None, current_ratio=None, lt_debt_to_equity=None, total_debt_to_equity=None,
               asset_turnover=None, inventory_turnover=None, revenue_per_employee=None, net_income_per_employee=None, receivable_turnover=None,
               dividend_yield=None, dividend_yield_5ya=None, dividend_growth_rate=None, payout_ratio=None):
        self._cur.execute("INSERT INTO %s VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" % self._table,
                          (self._today, pe_ratio, ps_ratio, cash_flow, free_cash_flow, pb_ratio, tangible_pb_ratio, gross_margin_ttm, gross_margin_5ya, operating_margin_ttm, operating_margin_5ya, pretax_margin_ttm, pretax_margin_5ya, net_profit_margin_ttm, net_profit_margin_5ya, revenue_per_share, basic_eps, diluted_eps, book_value_per_share, tangible_book_value_per_share, cash_per_share, cash_flow_per_share, return_on_equity_ttm, return_on_equity_5ya, return_on_assets_ttm, return_on_assets_5ya, return_on_investment_ttm, return_on_investment_5ya, eps_mrq_vs_mrq_1yr_ago, eps_ttm_vs_ttm_1yr_ago, eps_growth_5ya, sale_mrq_vs_qtr_1ya_ago, sale_ttm_vs_ttm_1ya_ago, sales_growth_5ya, capital_spending_growth_5ya, quick_ratio, current_ratio, lt_debt_to_equity, total_debt_to_equity, asset_turnover, inventory_turnover, revenue_per_employee, net_income_per_employee, receivable_turnover, dividend_yield, dividend_yield_5ya, dividend_growth_rate, payout_ratio))
        self._conn.commit()

    def view(self):
        self._cur.execute("SELECT * FROM %s" % self._table)
        rows = self._cur.fetchall()
        return rows

    def search(self, date=None, pe_ratio=None, ps_ratio=None, cash_flow=None, free_cash_flow=None, pb_ratio=None, tangible_pb_ratio=None,
               gross_margin_ttm=None, gross_margin_5ya=None, operating_margin_ttm=None, operating_margin_5ya=None, pretax_margin_ttm=None,
               pretax_margin_5ya=None, net_profit_margin_ttm=None, net_profit_margin_5ya=None, revenue_per_share=None, basic_eps=None,
               diluted_eps=None, book_value_per_share=None, tangible_book_value_per_share=None, cash_per_share=None, cash_flow_per_share=None,
               return_on_equity_ttm=None, return_on_equity_5ya=None, return_on_assets_ttm=None, return_on_assets_5ya=None,
               return_on_investment_ttm=None, return_on_investment_5ya=None, eps_mrq_vs_mrq_1yr_ago=None, eps_ttm_vs_ttm_1yr_ago=None,
               eps_growth_5ya=None, sale_mrq_vs_qtr_1ya_ago=None, sale_ttm_vs_ttm_1ya_ago=None, sales_growth_5ya=None,
               capital_spending_growth_5ya=None, quick_ratio=None, current_ratio=None, lt_debt_to_equity=None, total_debt_to_equity=None,
               asset_turnover=None, inventory_turnover=None, revenue_per_employee=None, net_income_per_employee=None, receivable_turnover=None,
               dividend_yield=None, dividend_yield_5ya=None, dividend_growth_rate=None, payout_ratio=None):
        self._cur.execute("SELECT * FROM %s WHERE date=? OR pe_ratio=? OR ps_ratio=? OR cash_flow=? OR free_cash_flow=? OR pb_ratio=? OR tangible_pb_ratio=? OR gross_margin_ttm=? OR gross_margin_5ya=? OR operating_margin_ttm=? OR operating_margin_5ya=? OR pretax_margin_ttm=? OR pretax_margin_5ya=? OR net_profit_margin_ttm=? OR net_profit_margin_5ya=? OR revenue_per_share=? OR basic_eps=? OR diluted_eps=? OR book_value_per_share=? OR tangible_book_value_per_share=? OR cash_per_share=? OR cash_flow_per_share=? OR return_on_equity_ttm=? OR return_on_equity_5ya=? OR return_on_assets_ttm=? OR return_on_assets_5ya=? OR return_on_investment_ttm=? OR return_on_investment_5ya=? OR eps_mrq_vs_mrq_1yr_ago=? OR eps_ttm_vs_ttm_1yr_ago=? OR eps_growth_5ya=? OR sale_mrq_vs_qtr_1ya_ago=? OR sale_ttm_vs_ttm_1ya_ago=? OR sales_growth_5ya=? OR capital_spending_growth_5ya=? OR quick_ratio=? OR current_ratio=? OR lt_debt_to_equity=? OR total_debt_to_equity=? OR asset_turnover=? OR inventory_turnover=? OR revenue_per_employee=? OR net_income_per_employee=? OR receivable_turnover=? OR dividend_yield=? OR dividend_yeild_5ya=? OR dividend_growth_rate=? OR payout_ratio=?" % self._table,
                          (date, pe_ratio, ps_ratio, cash_flow, free_cash_flow, pb_ratio, tangible_pb_ratio, gross_margin_ttm, gross_margin_5ya, operating_margin_ttm, operating_margin_5ya, pretax_margin_ttm, pretax_margin_5ya, net_profit_margin_ttm, net_profit_margin_5ya, revenue_per_share, basic_eps, diluted_eps, book_value_per_share, tangible_book_value_per_share, cash_per_share, cash_flow_per_share, return_on_equity_ttm, return_on_equity_5ya, return_on_assets_ttm, return_on_assets_5ya, return_on_investment_ttm, return_on_investment_5ya, eps_mrq_vs_mrq_1yr_ago, eps_ttm_vs_ttm_1yr_ago, eps_growth_5ya, sale_mrq_vs_qtr_1ya_ago, sale_ttm_vs_ttm_1ya_ago, sales_growth_5ya, capital_spending_growth_5ya, quick_ratio, current_ratio, lt_debt_to_equity, total_debt_to_equity, asset_turnover, inventory_turnover, revenue_per_employee, net_income_per_employee, receivable_turnover, dividend_yield, diviend_yield_5ya, dividend_growth_rate, payout_ratio))
        rows = self._cur.fetchall()
        return rows

    def update(self, id=0, pe_ratio=None, ps_ratio=None, cash_flow=None, free_cash_flow=None, pb_ratio=None, tangible_pb_ratio=None,
               gross_margin_ttm=None, gross_margin_5ya=None, operating_margin_ttm=None, operating_margin_5ya=None, pretax_margin_ttm=None,
               pretax_margin_5ya=None, net_profit_margin_ttm=None, net_profit_margin_5ya=None, revenue_per_share=None, basic_eps=None,
               diluted_eps=None, book_value_per_share=None, tangible_book_value_per_share=None, cash_per_share=None, cash_flow_per_share=None,
               return_on_equity_ttm=None, return_on_equity_5ya=None, return_on_assets_ttm=None, return_on_assets_5ya=None,
               return_on_investment_ttm=None, return_on_investment_5ya=None, eps_mrq_vs_mrq_1yr_ago=None, eps_ttm_vs_ttm_1yr_ago=None,
               eps_growth_5ya=None, sale_mrq_vs_qtr_1ya_ago=None, sale_ttm_vs_ttm_1ya_ago=None, sales_growth_5ya=None,
               capital_spending_growth_5ya=None, quick_ratio=None, current_ratio=None, lt_debt_to_equity=None, total_debt_to_equity=None,
               asset_turnover=None, inventory_turnover=None, revenue_per_employee=None, net_income_per_employee=None, receivable_turnover=None,
               dividend_yield=None, dividend_yield_5ya=None, dividend_growth_rate=None, payout_ratio=None):
        self._cur.execute("UPDATE %s SET pe_ratio=?, ps_ratio=?, cash_flow=?, free_cash_flow=?, pb_ratio=?, tangible_pb_ratio=?, gross_margin_ttm=?, gross_margin_5ya=?, operating_margin_ttm=?, operating_margin_5ya=?, pretax_margin_ttm=?, pretax_margin_5ya=?, net_profit_margin_ttm=?, net_profit_margin_5ya=?, revenue_per_share=?, basic_eps=?, diluted_eps=?, book_value_per_share=?, tangible_book_value_per_share=?, cash_per_share=?, cash_flow_per_share=?, return_on_equity_ttm=?, return_on_equity_5ya=?, return_on_assets_ttm=?, return_on_assets_5ya=?, return_on_investment_ttm=?, return_on_investment_5ya=?, eps_mrq_vs_mrq_1yr_ago=?, eps_ttm_vs_ttm_1yr_ago=?, eps_growth_5ya=?, sale_mrq_vs_qtr_1ya_ago=?, sale_ttm_vs_ttm_1ya_ago=?, sales_growth_5ya=?, capital_spending_growth_5ya=?, quick_ratio=?, current_ratio=?, lt_debt_to_equity=?, total_debt_to_equity=?, asset_turnover=?, inventory_turnover=?, revenue_per_employee=?, net_income_per_employee=?, receivable_turnover=?, dividend_yield=?, dividend_yeild_5ya=?, dividend_growth_rate=?, payout_ratio=? WHERE id=?" % self._table,
                         (pe_ratio, ps_ratio, cash_flow, free_cash_flow, pb_ratio, tangible_pb_ratio, gross_margin_ttm, gross_margin_5ya, operating_margin_ttm, operating_margin_5ya, pretax_margin_ttm, pretax_margin_5ya, net_profit_margin_ttm, net_profit_margin_5ya, revenue_per_share, basic_eps, diluted_eps, book_value_per_share, tangible_book_value_per_share, cash_per_share, cash_flow_per_share, return_on_equity_ttm, return_on_equity_5ya, return_on_assets_ttm, return_on_assets_5ya, return_on_investment_ttm, return_on_investment_5ya, eps_mrq_vs_mrq_1yr_ago, eps_ttm_vs_ttm_1yr_ago, eps_growth_5ya, sale_mrq_vs_qtr_1ya_ago, sale_ttm_vs_ttm_1ya_ago, sales_growth_5ya, capital_spending_growth_5ya, quick_ratio, current_ratio, lt_debt_to_equity, total_debt_to_equity, asset_turnover, inventory_turnover, revenue_per_employee, net_income_per_employee, receivable_turnover, dividend_yield, dividend_yield_5ya, dividend_growth_rate, payout_ratio,id))
        self._conn.commit()
        
    def remove_duplicate_rows(self):
        self._cur.execute("DELETE From %s WHERE id not in (SELECT max(id) from %s group by date, pe_ratio, ps_ratio, cash_flow, free_cash_flow, pb_ratio, tangible_pb_ratio, gross_margin_ttm, gross_margin_5ya, operating_margin_ttm, operating_margin_5ya, pretax_margin_ttm, pretax_margin_5ya, net_profit_margin_ttm, net_profit_margin_5ya, revenue_per_share, basic_eps, diluted_eps, book_value_per_share, tangible_book_value_per_share, cash_per_share, cash_flow_per_share, return_on_equity_ttm, return_on_equity_5ya, return_on_assets_ttm, return_on_assets_5ya, return_on_investment_ttm, return_on_investment_5ya, eps_mrq_vs_mrq_1yr_ago, eps_ttm_vs_ttm_1yr_ago, eps_growth_5ya, sale_mrq_vs_qtr_1ya_ago, sale_ttm_vs_ttm_1ya_ago, sales_growth_5ya, capital_spending_growth_5ya, quick_ratio, current_ratio, lt_debt_to_equity, total_debt_to_equity, asset_turnover, inventory_turnover, revenue_per_employee, net_income_per_employee, receivable_turnover, dividend_yield, dividend_yield_5ya, dividend_growth_rate, payout_ratio)" % (self._table, self._table))
        self._conn.commit()

    def delete(self, id):
        self._cur.execute("DELETE FROM %s WHERE id=?" % self._table,(id,))
        self._conn.commit()

    def __del__(self):
        self._conn.close()
