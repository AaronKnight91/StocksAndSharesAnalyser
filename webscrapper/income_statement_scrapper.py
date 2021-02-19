from selenium import webdriver
from base_scrapper import BaseScrapper

class IncomeStatement(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._button = self._soup.find_all("a",{"class","newBtn toggleButton LightGray"})

        #button = driver.find_element_by_class_name()

        driver = webdriver.Chrome()
        driver.get(webpage)
        print(driver.page_source)
        
def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-income-statement?cid=6661")
    #print(i._button)
    #print(i.html)

if __name__ == "__main__":
    main()
