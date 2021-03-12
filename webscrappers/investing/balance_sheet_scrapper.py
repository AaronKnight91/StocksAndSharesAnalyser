from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webscrappers.base_scrapper import BaseScrapper

class IncomeStatement(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)

        # Scrape quartly income statements
        self._table = self._soup.find_all("table", {"class":"genTbl reportTbl"})
        self._th = self._table[0].find_all("th")
        self._tr = self._soup.find_all("tr")

        for ind, i in enumerate(self._th):
            if ind == 0:
                continue
            self._period = self.get_periods(i)
            self._total_current_assets = self.get_total_current_assets(ind)
            self._cash_and_short_term_investments = self.get_cash_and_short_term_investments(ind)
            self._cash = self.get_cash(ind)
            self._cash_and_equivalents = self.get_cash_and_equivalents(ind)
            self._short_term_investments = self.get_short_term_investments(ind)
            self._total_net_receivables = self.get_total_net_receivables(ind)
            self._accounts_receivables = self.get_accounts_receivables(ind)
            self._total_inventory = self.get_total_inventory(ind)
            self._prepaid_expenses = self.get_prepaid_expenses(ind)
            self._total_other_current_assets = self.get_total_other_current_assets(ind)

            self._total_assets = self.get_total_assets(ind)
            self._total_net_ppe = self.get_total_net_ppe(ind)
            self._total_accumulated_depreciation = self.get_total_accumulated_depreciation(ind)
            self._net_goodwill = self.get_net_goodwill(ind)
            self._net_intangibles = self.get_net_intangibles(ind)
            self._long_term_investments = self.get_long_term_investments(ind)
            self._long_term_note_receivables = self.get_long_term_note_receivables(ind)
            self._total_other_long_term_assets = self.get_total_other_long_term_assets(ind)
            self._total_other_assets = self.get_total_other_assets(ind)

            self._total_current_liabilities = self.get_total_current_liabilities(ind)
            self._accounts_payable = self.get_accounts_payable(ind)
            self._payable_accrued = self.get_payable_accrued(ind)
            self._accrued_expenses = self.get_accrued_expenses(ind)
            self._short_term_debt = self.get_short_term_debt(ind)
            self._capital_leases = self.get_capital_leases(ind)
            self._total_other_current_liabilities = self.get_total_other_current_liabilities(ind)
            
            self._total_liabilities = self.get_total_liabilities(ind)
            self._total_long_term_debt = self.get_total_long_term_debt(ind)
            self._capital_lease_obligations = self.get_capital_lease_obligations(ind)
            self._deferred_income_tax = self.get_deferred_income_tax(ind)
            self._minority_interest = self.get_minority_interest(ind)
            self._total_other_liabilities = self.get_total_other_liabilities(ind)

            self._total_equity = self.get_total_equity(ind)
            self._total_redeemable_preferred_stock = self.get_total_redeemable_preferred_stock(ind)
            self._preferred_stock_non_redeemable = self.get_preferred_stock_non_redeemable(ind)
            self._total_common_stock = self.get_total_common_stock(ind)
            self._additional_pain_in_capital = self.get_additional_pain_in_capital(ind)
            self._retained_earnings = self.get_retained_earnings(ind)
            self._common_treasury_stock = self.get_common_treasury_stock(ind)
            self._esop_debt_guarantee = self.get_esop_debt_guarantee(ind)
            self._unrealised_gain = self.get_unrealised_gain(ind)
            self._total_other_equity = self.get_total_other_equity(ind)

            self._total_liabilities_and_shareholders_equity = self.get_total_liabilities_and_shareholders_equity(ind)
            self._total_common_shares_outstanding = self.get_total_common_shares_outstanding(ind)
            self._total_preferred_shares_outstanding = self.get_total_preferred_shares_outstanding(ind)
            
        #button = driver.find_element_by_class_name()

        #option = webdriver.ChromeOptions()
        #option.add_argument('headqless')
        #driver = webdriver.Chrome(options=option)
        #driver.get(webpage)
        #button = driver.find_element_by_xpath("//a[@class='newBtn toggleButton LightGray']")
        #print(len(button))
        #button.click()
        #print(driver.page_source)
        
        #button = driver.find_element_by_css_selector("newBtn toggleButton LightGray")


    def get_periods(self, i):
            year = i.text[0:4]
            month = i.text[4:]

    def get_total_current_assets(self, ind):
        td = self._tr[10].findAll("td")[ind]
        return td.text
            
    def get_cash_and_short_term_investments(self, ind):
        td = self._tr[11].findAll("td")[ind]
        return td.text

    def get_cash(self, ind):
        td = self._tr[12].findAll("td")[ind]
        return td.text
        
    def get_cash_and_equivalents(self, ind):
        td = self._tr[13].findAll("td")[ind]
        return td.text

    def get_short_term_investments(self, ind):
        td = self._tr[14].findAll("td")[ind]
        return td.text

    def get_total_net_receivables(self, ind):
        td = self._tr[15].findAll("td")[ind]
        return td.text

    def get_accounts_receivables(self, ind):
        td = self._tr[16].findAll("td")[ind]
        return td.text

    def get_total_inventory(self, ind):
        td = self._tr[17].findAll("td")[ind]
        return td.text

    def get_prepaid_expenses(self, ind):
        td = self._tr[18].findAll("td")[ind]
        return td.text

    def get_total_other_current_assets(self, ind):
        td = self._tr[19].findAll("td")[ind]
        return td.text

    def get_total_assets(self, ind):
        td = self._tr[20].findAll("td")[ind]
        return td.text

    def get_total_net_ppe(self, ind):
        td = self._tr[21].findAll("td")[ind]
        return td.text

    def get_total_accumulated_depreciation(self, ind):
        td = self._tr[22].findAll("td")[ind]
        return td.text

    def get_net_goodwill(self, ind):
        td = self._tr[23].findAll("td")[ind]
        return td.text

    def get_net_intangibles(self, ind):
        td = self._tr[24].findAll("td")[ind]
        return td.text

    def get_long_term_investments(self, ind):
        td = self._tr[25].findAll("td")[ind]
        return td.text

    def get_long_term_note_receivables(self, ind):
        td = self._tr[26].findAll("td")[ind]
        return td.text

    def get_total_other_long_term_assets(self, ind):
        td = self._tr[27].findAll("td")[ind]
        return td.text

    def get_total_other_assets(self, ind):
        td = self._tr[28].findAll("td")[ind]
        return td.text

    def get_total_current_liabilities(self, ind):
        td = self._tr[29].findAll("td")[ind]
        return td.text
        
    def get_accounts_payable(self, ind):
        td = self._tr[30].findAll("td")[ind]
        return td.text
        
    def get_payable_accrued(self, ind):
        td = self._tr[31].findAll("td")[ind]
        return td.text
        
    def get_accrued_expenses(self, ind):
        td = self._tr[32].findAll("td")[ind]
        return td.text

    def get_short_term_debt(self, ind):
        td = self._tr[33].findAll("td")[ind]
        return td.text
        
    def get_capital_leases(self, ind):
        td = self._tr[34].findAll("td")[ind]
        return td.text

    def get_total_other_current_liabilities(self, ind):
        td = self._tr[35].findAll("td")[ind]
        return td.text
            
    def get_total_liabilities(self, ind):
        td = self._tr[36].findAll("td")[ind]
        return td.text
        
    def get_total_long_term_debt(self, ind):
        td = self._tr[37].findAll("td")[ind]
        return td.text
        
    def get_capital_lease_obligations(self, ind):
        td = self._tr[38].findAll("td")[ind]
        return td.text
        
    def get_deferred_income_tax(self, ind):
        td = self._tr[39].findAll("td")[ind]
        return td.text
        
    def get_minority_interest(self, ind):
        td = self._tr[40].findAll("td")[ind]
        return td.text
        
    def get_total_other_liabilities(self, ind):
        td = self._tr[41].findAll("td")[ind]
        return td.text
        
    def get_total_equity(self, ind):
        td = self._tr[42].findAll("td")[ind]
        return td.text
        
    def get_total_redeemable_preferred_stock(self, ind):
        td = self._tr[43].findAll("td")[ind]
        return td.text
        
    def get_preferred_stock_non_redeemable(self, ind):
        td = self._tr[44].findAll("td")[ind]
        return td.text
        
    def get_total_common_stock(self, ind):
        td = self._tr[45].findAll("td")[ind]
        return td.text
        
    def get_additional_pain_in_capital(self, ind):
        td = self._tr[46].findAll("td")[ind]
        return td.text
        
    def get_retained_earnings(self, ind):
        td = self._tr[47].findAll("td")[ind]
        return td.text
        
    def get_common_treasury_stock(self, ind):
        td = self._tr[48].findAll("td")[ind]
        return td.text
        
    def get_esop_debt_guarantee(self, ind):
        td = self._tr[49].findAll("td")[ind]
        return td.text
        
    def get_unrealised_gain(self, ind):
        td = self._tr[50].findAll("td")[ind]
        return td.text
        
    def get_total_other_equity(self, ind):
        td = self._tr[51].findAll("td")[ind]
        return td.text

    def get_total_liabilities_and_shareholders_equity(self, ind):
        td = self._tr[52].findAll("td")[ind]
        return td.text
        
    def get_total_common_shares_outstanding(self, ind):
        td = self._tr[53].findAll("td")[ind]
        return td.text
        
    def get_total_preferred_shares_outstanding(self, ind):
        td = self._tr[54].findAll("td")[ind]
        return td.text
            

def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-balance-sheet?cid=6661")

if __name__ == "__main__":
    main()
