from selenium import webdriver
from base_scrapper import BaseScrapper

class IncomeStatement(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._table = self._soup.find_all("table", {"class":"genTbl reportTbl"})
        self._th = self._table[0].find_all("th")
        self._tr = self._soup.find_all("tr")

        for ind, i in enumerate(self._th):
            if ind == 0:
                continue
            self._period = self.get_periods(i)
            self._total_revenue = self.get_total_revenue(ind)
            self._revenue = self.get_revenue(ind)
            self._other_revenue = self.get_other_revenue(ind)
            self._cost_of_revenue = self.get_cost_of_revenue(ind)
            self._gross_profit = self.get_gross_profit(ind)
            self._total_operating_expenses = self.get_total_operating_expenses(ind)
            self._total_sga_expenses = self.get_total_sga_expenses(ind+1)
            self.get_research_and_development(ind)
            self.get_depreciation(ind)
            self.get_interest_expense(ind)
            self.get_unusual_expense(ind)
            self.get_other_expenses(ind)
            self.get_operating_income(ind)
            self.get_interest_income(ind)
            self.get_gain_on_sale(ind)
            self.get_other_net(ind)
            self.get_net_income_before_taxes(ind)
            self.get_provision_income_taxes(ind)
            self.get_net_income_taxes(ind)
            self.get_minority_interest(ind)
            self.get_equity_in_affiliates(ind)
            self.get_us_gaap_adjustment(ind)
            self.get_net_income_before_extraordinary_items(ind)
            self.get_total_extraordinary_items(ind)
            self.get_net_income(ind)
            self.get_total_adjustments_to_net_income(ind)
            self.get_income_aval_to_common(ind)
            self.get_dilution_adjustment(ind)
            self.get_diluted_net_income(ind)
            self.get_diluted_weighted_average_shares(ind)
            self.get_diluted_eps(ind)
            self.get_dps(ind)
            self.get_diluted_normalised_eps(ind)
            
        #button = driver.find_element_by_class_name()

        #driver = webdriver.Chrome()
        #driver.get(webpage)
        #print(driver.page_source)

        #button = driver.find_element_by_css_selector("newBtn toggleButton LightGray")


    def get_periods(self, i):
            year = i.text[0:4]
            month = i.text[4:]

    def get_total_revenue(self, ind):
        td = self._tr[10].findAll("td")[ind]
        return td.text
            
    def get_revenue(self, ind):
        td = self._tr[11].findAll("td")[ind]
        return td.text

    def get_other_revenue(self, ind):
        td = self._tr[12].findAll("td")[ind]
        return td.text
        
    def get_cost_of_revenue(self, ind):
        td = self._tr[13].findAll("td")[ind]
        return td.text

    def get_gross_profit(self, ind):
        td = self._tr[14].findAll("td")[ind]
        return td.text

    def get_total_operating_expenses(self, ind):
        td = self._tr[15].findAll("td")[ind]
        return td.text

    def get_total_sga_expenses(self, ind):
        td = self._tr[16].findAll("td")[ind]
        return td.text

    def get_research_and_development(self, ind):
        td = self._tr[17].findAll("td")[ind]
        #print(td.text)

    def get_depreciation(self, ind):
        td = self._tr[18].findAll("td")[ind]

    def get_interest_expense(self, ind):
        td = self._tr[19].findAll("td")[ind]

    def get_unusual_expense(self, ind):
        td = self._tr[20].findAll("td")[ind]

    def get_other_expenses(self, ind):
        td = self._tr[21].findAll("td")[ind]

    def get_operating_income(self, ind):
        td = self._tr[22].findAll("td")[ind]

    def get_interest_income(self, ind):
        td = self._tr[23].findAll("td")[ind]

    def get_gain_on_sale(self, ind):
        td = self._tr[24].findAll("td")[ind]

    def get_other_net(self, ind):
        td = self._tr[25].findAll("td")[ind]

    def get_net_income_before_taxes(self, ind):
        td = self._tr[26].findAll("td")[ind]

    def get_provision_income_taxes(self, ind):
        td = self._tr[27].findAll("td")[ind]

    def get_net_income_taxes(self, ind):
        td = self._tr[28].findAll("td")[ind]

    def get_minority_interest(self, ind):
        td = self._tr[29].findAll("td")[ind]

    def get_equity_in_affiliates(self, ind):
        td = self._tr[30].findAll("td")[ind]

    def get_us_gaap_adjustment(self, ind):
        td = self._tr[31].findAll("td")[ind]

    def get_net_income_before_extraordinary_items(self, ind):
        td = self._tr[32].findAll("td")[ind]

    def get_total_extraordinary_items(self, ind):
        td = self._tr[33].findAll("td")[ind]

    def get_net_income(self, ind):
        td = self._tr[34].findAll("td")[ind]

    def get_total_adjustments_to_net_income(self, ind):
        td = self._tr[36].findAll("td")[ind]

    def get_income_aval_to_common(self, ind):
        td = self._tr[37].findAll("td")[ind]

    def get_dilution_adjustment(self, ind):
        td = self._tr[38].findAll("td")[ind]

    def get_diluted_net_income(self, ind):
        td = self._tr[39].findAll("td")[ind]

    def get_diluted_weighted_average_shares(self, ind):
        td = self._tr[40].findAll("td")[ind]

    def get_diluted_eps(self, ind):
        td = self._tr[41].findAll("td")[ind]

    def get_dps(self, ind):
        td = self._tr[42].findAll("td")[ind]

    def get_diluted_normalised_eps(self, ind):
        td = self._tr[43].findAll("td")[ind]


def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-income-statement?cid=6661")

if __name__ == "__main__":
    main()
