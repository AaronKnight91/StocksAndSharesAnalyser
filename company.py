from urllib.request import Request, urlopen
import bs4

class Company:

    def __init__(self, webpage):

        self._webpage = webpage
        self._html = self.get_webpage()

        self._pe_ratio = self.get_pe_ratio()

    def get_webpage(self):
        req = Request(self._webpage, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        soup = bs4.BeautifulSoup(webpage,"html.parser")
        all = soup.find_all("tr",{"class":"child"})

        result = all[0].find_all("td",{"class":""})

        return result

    def get_pe_ratio(self):
        return self._html[1].text
        
company = Company("https://uk.investing.com/equities/avast-holdings-ratios")
print(company._pe_ratio)
