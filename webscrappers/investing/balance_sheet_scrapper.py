from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from base_scrapper import BaseScrapper

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
            self._operating_income = self.get_operating_income(ind)
            self._interest_income = self.get_interest_income(ind)
            self._gain_on_sale = self.get_gain_on_sale(ind)
            self._other_net = self.get_other_net(ind)
            self._net_income_before_taxes = self.get_net_income_before_taxes(ind)
            self._provision_income_taxes = self.get_provision_income_taxes(ind)
            self._net_income_taxes = self.get_net_income_taxes(ind)
            self._minority_interest = self.get_minority_interest(ind)
            self._equity_in_affiliates = self.get_equity_in_affiliates(ind)
            self._us_gaap_adjustment = self.get_us_gaap_adjustment(ind)
            self._net_income_before_extra_items = self.get_net_income_before_extraordinary_items(ind)
            self._total_extra_items = self.get_total_extraordinary_items(ind)
            self._new_income = self.get_net_income(ind)
            self._total_adjustments_to_net_income = self.get_total_adjustments_to_net_income(ind)
            self._income_aval_to_common = self.get_income_aval_to_common(ind)
            self._dilution_adjustment = self.get_dilution_adjustment(ind)
            self._diluted_net_income = self.get_diluted_net_income(ind)
            self._diluted_weighted_average_shares = self.get_diluted_weighted_average_shares(ind)
            self._diluted_eps = self.get_diluted_eps(ind)
            self._dps = self.get_dps(ind)
            self._diluted_normalised_eps = self.get_diluted_normalised_eps(ind)
            
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

    def get_operating_income(self, ind):
        td = self._tr[22].findAll("td")[ind]
        return td.text

    def get_interest_income(self, ind):
        td = self._tr[23].findAll("td")[ind]
        return td.text

    def get_gain_on_sale(self, ind):
        td = self._tr[24].findAll("td")[ind]
        return td.text

    def get_other_net(self, ind):
        td = self._tr[25].findAll("td")[ind]
        return td.text

    def get_net_income_before_taxes(self, ind):
        td = self._tr[26].findAll("td")[ind]
        return td.text

    def get_provision_income_taxes(self, ind):
        td = self._tr[27].findAll("td")[ind]
        return td.text

    def get_net_income_taxes(self, ind):
        td = self._tr[28].findAll("td")[ind]
        return td.text

    def get_minority_interest(self, ind):
        td = self._tr[29].findAll("td")[ind]
        return td.text

    def get_equity_in_affiliates(self, ind):
        td = self._tr[30].findAll("td")[ind]
        return td.text

    def get_us_gaap_adjustment(self, ind):
        td = self._tr[31].findAll("td")[ind]
        return td.text

    def get_net_income_before_extraordinary_items(self, ind):
        td = self._tr[32].findAll("td")[ind]
        return td.text

    def get_total_extraordinary_items(self, ind):
        td = self._tr[33].findAll("td")[ind]
        return td.text

    def get_net_income(self, ind):
        td = self._tr[34].findAll("td")[ind]
        return td.text

    def get_total_adjustments_to_net_income(self, ind):
        td = self._tr[36].findAll("td")[ind]
        return td.text

    def get_income_aval_to_common(self, ind):
        td = self._tr[37].findAll("td")[ind]
        return td.text

    def get_dilution_adjustment(self, ind):
        td = self._tr[38].findAll("td")[ind]
        return td.text

    def get_diluted_net_income(self, ind):
        td = self._tr[39].findAll("td")[ind]
        return td.text

    def get_diluted_weighted_average_shares(self, ind):
        td = self._tr[40].findAll("td")[ind]
        return td.text

    def get_diluted_eps(self, ind):
        td = self._tr[41].findAll("td")[ind]
        return td.text

    def get_dps(self, ind):
        td = self._tr[42].findAll("td")[ind]
        return td.text

    def get_diluted_normalised_eps(self, ind):
        td = self._tr[43].findAll("td")[ind]
        return td.text


def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-balance-sheet?cid=6661")

if __name__ == "__main__":
    main()
