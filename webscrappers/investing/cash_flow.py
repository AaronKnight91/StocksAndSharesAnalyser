
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webscrappers.base_scrapper import BaseScrapper

class CashFlow(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)

        # Scrape quartly income statements
        self._table = self._soup.find_all("table", {"class":"genTbl reportTbl"})
        #self._th = self._table[0].find_all("th")
        self._tr = self._soup.find_all("tr")

        self._th = self._tr[0].find_all("th")
        
        for ind, i in enumerate(self._th):
            if ind == 0:
                continue
            self._period = self.get_periods(i)

            self._net_income = self.get_net_income(ind)
            
            self._cash_from_operating_activities = self.get_cash_from_operating_activities(ind)
            self._depreciation = self.get_depreciation(ind)
            self._amortization = self.get_amortizatin(ind)
            self._deferred_taxes = self.get_deferred_taxes(ind)
            self._non_cash_items = self.get_non_cash_items(ind)
            self._cash_receipts = self.get_cash_receipts(ind)
            self._cash_payments = self.get_cash_payments(ind)
            self._cash_taxes_paid = self.get_cash_taxes_paid(ind)
            self._cash_interest_paid = self.get_cash_interest_paid(ind)
            self._changes_in_working_capital = self.get_changes_in_working_capital(ind)
            
            self._cash_from_investing_activities = self.get_cash_from_investing_activities(ind)
            self._capital_expenditures = self.get_capital_expenditures(ind)
            self._total_other_investing_cash_flow_items = self.get_total_other_investiving_cash_flow_items(ind)
            
            self._cash_from_financing_activities = self.get_cash_from_financing_activities(ind)
            self._financing_cash_flow_items = self.get_financing_cash_flow_items(ind)
            self._total_cash_dividends_paid = self.get_total_cash_dividends_paid(ind)
            self._net_insurance_of_stock = self.get_net_insurance_of_stock(ind)
            self._net_insurance_of_debt = self.get_net_insurance_of_debt(ind)

            self._foreign_exchange_effects = self.get_foreign_exchange_effects(ind)

            self._net_change_in_cash = self.get_net_change_in_cash(ind)

            self._beginning_cash_balance = self.get_beginning_cash_balance(ind)
            
            self._ending_cash_balance = self.get_ending_cash_balance(ind)

            self._free_cash_flow = self.get_free_cash_flow(ind)
            
            self._free_cash_flow_growth = self.get_free_cash_flow_growth(ind)

            self._free_cash_flow_yield = self.get_free_cash_flow_yield(ind)

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

    def get_net_income(self, ind):
        td = self._tr[10].findAll("td")[ind]
        return td.text
            
    def get_cash_from_operating_activities(self, ind):
        td = self._tr[11].findAll("td")[ind]
        return td.text
        
    def get_depreciation(self, ind):
        td = self._tr[12].findAll("td")[ind]
        return td.text
        
    def get_amortizatin(self, ind):
        td = self._tr[13].findAll("td")[ind]
        return td.text
        
    def get_deferred_taxes(self, ind):
        td = self._tr[14].findAll("td")[ind]
        return td.text
        
    def get_non_cash_items(self, ind):
        td = self._tr[15].findAll("td")[ind]
        return td.text
        
    def get_cash_receipts(self, ind):
        td = self._tr[16].findAll("td")[ind]
        return td.text
        
    def get_cash_payments(self, ind):
        td = self._tr[17].findAll("td")[ind]
        return td.text
        
    def get_cash_taxes_paid(self, ind):
        td = self._tr[18].findAll("td")[ind]
        return td.text
        
    def get_cash_interest_paid(self, ind):
        td = self._tr[19].findAll("td")[ind]
        return td.text
        
    def get_changes_in_working_capital(self, ind):
        td = self._tr[20].findAll("td")[ind]
        return td.text
            
    def get_cash_from_investing_activities(self, ind):
        td = self._tr[21].findAll("td")[ind]
        return td.text
        
    def get_capital_expenditures(self, ind):
        td = self._tr[22].findAll("td")[ind]
        return td.text
        
    def get_total_other_investiving_cash_flow_items(self, ind):
        td = self._tr[23].findAll("td")[ind]
        return td.text
            
    def get_cash_from_financing_activities(self, ind):
        td = self._tr[24].findAll("td")[ind]
        return td.text
        
    def get_financing_cash_flow_items(self, ind):
        td = self._tr[25].findAll("td")[ind]
        return td.text
        
    def get_total_cash_dividends_paid(self, ind):
        td = self._tr[26].findAll("td")[ind]
        return td.text
        
    def get_net_insurance_of_stock(self, ind):
        td = self._tr[27].findAll("td")[ind]
        return td.text
        
    def get_net_insurance_of_debt(self, ind):
        td = self._tr[28].findAll("td")[ind]
        return td.text

    def get_foreign_exchange_effects(self, ind):
        td = self._tr[29].findAll("td")[ind]
        return td.text

    def get_net_change_in_cash(self, ind):
        td = self._tr[30].findAll("td")[ind]
        return td.text

    def get_beginning_cash_balance(self, ind):
        td = self._tr[31].findAll("td")[ind]
        return td.text
            
    def get_ending_cash_balance(self, ind):
        td = self._tr[31].findAll("td")[ind]
        return td.text

    def get_free_cash_flow(self, ind):
        td = self._tr[32].findAll("td")[ind]
        return td.text
            
    def get_free_cash_flow_growth(self, ind):
        td = self._tr[33].findAll("td")[ind]
        return td.text

    def get_free_cash_flow_yield(self, ind):
        td = self._tr[34].findAll("td")[ind]
        return td.text

def main():

    i = CashFlow("https://uk.investing.com/equities/unilever-ord-cash-flow?cid=6661")

if __name__ == "__main__":
    main()
