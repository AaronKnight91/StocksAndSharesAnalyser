import Selenium
from base_scrapper import BaseScrapper

class IncomeStatement(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._html = self._soup.find_all("tr")


def main():

    i = IncomeStatement("https://uk.investing.com/equities/unilever-ord-income-statement?cid=6661")
    print(i._html)

if __name__ == "__main__":
    main()
