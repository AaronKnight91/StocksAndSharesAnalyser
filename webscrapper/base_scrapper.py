from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError, ContentTooShortError
import bs4

class BaseScrapper:

    """
    The company class stores metrics for analysis.
    The metrics are taken from uk.investing.com.
    """

    def __init__(self, webpage):

        self._webpage = webpage
        self._soup = self.get_webpage()
        
            
    def get_webpage(self):
        try:
            req = Request(self._webpage, headers={'User-Agent':'Mozilla/5.0'})
            webpage = urlopen(req, timeout=30).read()
            soup = bs4.BeautifulSoup(webpage,"html.parser")
            #all = soup.find_all("tr",{"class":"child"})
        
            return soup#all
        
        except URLError as urlerror:
            print("[ERROR]:", urlerror)
            return None
        except HTTPError as httperror:
            print("[ERROR]:",httperror)
            return None
        except ContentTooShortError as ctserror:
            print("[ERROR]:",ctserror)
            return None
        except Exception as error:
            print("[ERROR]:", error)
            return None
