from selenium import webdriver
from base_scrapper import BaseScrapper

class IncomeStatement(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._html = self._soup.find_all("table", {"class":"genTbl reportTbl"})
        self._th = self._html[0].find_all("th")
        self._button = self._soup.find_all("a",{"class","newBtn toggleButton LightGray"})


        for ind, i in enumerate(self._th):
            if ind == 0:
                continue
            self.get_periods(i)
            self.get_total_revenue(ind)
            self.get_revenue(ind)
            self.get_other_revenue(ind)
            #self.get_cost_of_revenue(ind)
            
        #button = driver.find_element_by_class_name()

        #driver = webdriver.Chrome()
        #driver.get(webpage)
        #print(driver.page_source)

        #button = driver.find_element_by_css_selector("newBtn toggleButton LightGray")


    def get_periods(self, i):
            year = i.text[0:4]
            month = i.text[4:]

    def get_total_revenue(self, ind):
        tr = self._html[1].findAll("tr")[0]
        print(tr)
        #td = tr.findAll("td")[ind].text
        #print(td)
            
    def get_revenue(self, ind):
        tr = self._html[1].findAll("tr")[0]
        td = tr.findAll("td")[ind].text

    def get_other_revenue(self, ind):
        tr = self._html[1].findAll("tr")[1]
        td = tr.findAll("td")[ind].text
        print(td)

    def get_cost_of_revenue(self, ind):
        tr = self._html[1].findAll("tr")[2]
        print(tr)

def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-income-statement?cid=6661")

if __name__ == "__main__":
    main()
