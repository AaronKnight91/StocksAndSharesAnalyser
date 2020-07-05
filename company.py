from urllib.request import Request, urlopen
import bs4

class Company:

    """
    The company class stores metrics for analysis.
    The metrics are taken from uk.investing.com.
    """

    def __init__(self, webpage):

        self._webpage = webpage
        self._html = self.get_webpage()

        self._pe_ratio = self.get_pe_ratio()
        self._ps_ratio = self.get_ps_ratio()
        self._cash_flow = self.get_cash_flow()
        self._free_cash_flow = self.get_free_cash_flow()
        self._pb_ratio = self.get_pb_ratio()
        self._tangible_pb_ratio = self.get_tangible_pb_ratio()

        self._gross_margin_ttm = self.get_gross_margin_ttm()
        self._gross_margin_5ya = self.get_gross_margin_5ya()
        self._operating_margin_ttm = self.get_operating_margin_ttm()
        self._operating_margin_5ya = self.get_operating_margin_5ya()
        self._pretax_margin_ttm = self.get_pretax_margin_ttm()
        self._pretax_margin_5ya = self.get_pretax_margin_5ya()
        self._net_profit_margin_ttm = self.get_net_profit_margin_ttm()
        self._net_profit_margin_5ya = self.get_net_profit_margin_5ya()

        self._revenue_per_share = self.get_revenue_per_share()
        self._basic_eps = self.get_basic_eps()
        self._diluted_eps = self.get_diluted_eps()
        
        self._debt_to_equity = self.get_debt_to_equity()
        self._dividend_yield = self.get_dividend_yield()
        self._payout_ratio = self.get_payout_ratio()
        
    def get_webpage(self):
        req = Request(self._webpage, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        soup = bs4.BeautifulSoup(webpage,"html.parser")
        all = soup.find_all("tr",{"class":"child"})
        
        return all

    def get_pe_ratio(self):
        try:
            pe_ratio = self._html[0].find_all("td",{"class":""})
            if pe_ratio[1].text.replace(",","") == "-" or pe_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pe_ratio[1].text.replace(",",""))
        except:
            return -999
        
    def get_ps_ratio(self):
        try:
            ps_ratio = self._html[1].find_all("td",{"class":""})
            if ps_ratio[1].text.replace(",","") == "-" or ps_ratio[1].text.replace(",","") == "" :
                return -999
            else:
                return float(ps_ratio[1].text.replace(",",""))
        except:
            return -999
        
    def get_cash_flow(self):
        try:
            cash_flow = self._html[2].find_all("td",{"class":""})
            if cash_flow[1].text.replace(",","") == "-" or cash_flow[1].text.replace(",","") == "":
                    return -999
            else:
                return float(cash_flow[1].text.replace(",",""))
        except:
            return -999

    def get_free_cash_flow(self):
        try:
            cash_flow = self._html[3].find_all("td",{"class":""})
            if cash_flow[1].text.replace(",","") == "-" or cash_flow[1].text.replace(",","") == "":
                    return -999
            else:
                return float(cash_flow[1].text.replace(",",""))
        except:
            return -999

    def get_pb_ratio(self):
        try:
            pb_ratio = self._html[4].find_all("td",{"class":""})
            if pb_ratio[1].text.replace(",","") == "-" or pb_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pb_ratio[1].text.replace(",",""))
        except:
            return -999

    def get_tangible_pe_ratio(self):
        try:
            pb_ratio = self._html[5].find_all("td",{"class":""})
            if pb_ratio[1].text.replace(",","") == "-" or pb_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pb_ratio[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_gross_margin_ttm(self):
        try:
            gross_margin = self._html[6].find_all("td",{"class":""})
            if gross_margin[1].text.replace(",","") == "-" or gross_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(gross_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_gross_margin_5ya(self):
        try:
            gross_margin = self._html[7].find_all("td",{"class":""})
            if gross_margin[1].text.replace(",","") == "-" or gross_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(gross_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_operating_margin_ttm(self):
        try:
            operating_margin = self._html[8].find_all("td",{"class":""})
            if operating_margin[1].text.replace(",","") == "-" or operating_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(operating_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_operating_margin_5ya(self):
        try:
            operating_margin = self._html[9].find_all("td",{"class":""})
            if operating_margin[1].text.replace(",","") == "-" or operating_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(operating_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_pretax_margin_ttm(self):
        try:
            pretax_margin = self._html[10].find_all("td",{"class":""})
            if pretax_margin[1].text.replace(",","") == "-" or pretax_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(pretax_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_pretax_margin_5ya(self):
        try:
            pretax_margin = self._html[11].find_all("td",{"class":""})
            if pretax_margin[1].text.replace(",","") == "-" or pretax_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(pretax_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_net_profit_margin_ttm(self):
        try:
            net_profit_margin = self._html[12].find_all("td",{"class":""})
            if net_profit_margin[1].text.replace(",","") == "-" or net_profit_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(net_profit_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_net_profit_margin_5ya(self):
        try:
            net_profit_margin = self._html[13].find_all("td",{"class":""})
            if net_profit_margin[1].text.replace(",","") == "-" or net_profit_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(net_profit_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_revenue_per_share(self):
        try:
            revenue_per_share = self._html[14].find_all("td",{"class":""})
            if revenue_per_share[1].text.replace(",","") == "-" or revenue_per_share[1].text.replace(",","") == "":
                return -999
            else:
                return float(revenue_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_basic_eps(self):
        try:
            basic_eps = self._html[15].find_all("td",{"class":""})
            if basic_eps[1].text.repace(",","") == "-" or basic_eps[1].text.repace(",","") == "":
                return -999
            else:
                return float(basic_eps[1].text.replace(",",""))
        except:
            return -999

    def get_diluted_eps(self):
        try:
            diluted_eps = self._html[15].find_all("td",{"class":""})
            if diluted_eps[1].text.repace(",","") == "-" or diluted_eps[1].text.repace(",","") == "":
                return -999
            else:
                return float(diluted_eps[1].text.replace(",",""))
        except:
            return -999
        











        





        
    def get_debt_to_equity(self):
        try:
            debt_to_equity = self._html[39].find_all("td",{"class":""})
            if debt_to_equity[1].text[:-1].replace(",","") == "-" or debt_to_equity[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(debt_to_equity[1].text[:-1].replace(",",""))
        except:
            return -999
        
    def get_dividend_yield(self):
        try:
            dividend_yield = self._html[45].find_all("td",{"class":""})
            if dividend_yield[1].text[:-1].replace(",","") == "-" or dividend_yield[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(dividend_yield[1].text[:-1].replace(",",""))
        except:
            return -999
            
    def get_payout_ratio(self):
        try:
            payout_ratio = self._html[48].find_all("td",{"class":""})
            if payout_ratio[1].text[:-1].replace(",","") == "-" or payout_ratio[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(payout_ratio[1].text[:-1].replace(",",""))
        except:
            return -999
        
#company = Company("https://uk.investing.com/equities/avast-holdings-ratios")
#print(company._pe_ratio)
#print(company._ps_ratio)
#print(company._cash_flow)
#print(company._pb_ratio)
#print(company._dividend_yield)
#print(company._payout_ratio)
