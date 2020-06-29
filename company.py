from urllib.request import Request, urlopen
import bs4

class Company:

    def __init__(self, webpage):

        self._webpage = webpage
        self._html = self.get_webpage()

        self._pe_ratio = self.get_pe_ratio()
        self._ps_ratio = self.get_ps_ratio()
        self._cash_flow = self.get_cash_flow()
        self._pb_ratio = self.get_pb_ratio()
        self._dividend_yield = self.get_dividend_yield()
        self._payout_ratio = self.get_payout_ratio()
        
    def get_webpage(self):
        req = Request(self._webpage, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        soup = bs4.BeautifulSoup(webpage,"html.parser")
        all = soup.find_all("tr",{"class":"child"})
        
        return all

    def get_pe_ratio(self):
        pe_ratio = self._html[0].find_all("td",{"class":""})
        return pe_ratio[1].text

    def get_ps_ratio(self):
        ps_ratio = self._html[1].find_all("td",{"class":""})
        return ps_ratio[1].text

    def get_cash_flow(self):
        cash_flow = self._html[3].find_all("td",{"class":""})
        return cash_flow[1].text

    def get_pb_ratio(self):
        pb_ratio = self._html[4].find_all("td",{"class":""})
        return pb_ratio[1].text

    def get_dividend_yield(self):
        dividend_yield = self._html[45].find_all("td",{"class":""})
        return dividend_yield[1].text[:-1]

    def get_payout_ratio(self):
        payout_ratio = self._html[48].find_all("td",{"class":""})
        return payout_ratio[1].text[:-1]
    
#company = Company("https://uk.investing.com/equities/avast-holdings-ratios")
#print(company._pe_ratio)
#print(company._ps_ratio)
#print(company._cash_flow)
#print(company._pb_ratio)
#print(company._dividend_yield)
#print(company._payout_ratio)
