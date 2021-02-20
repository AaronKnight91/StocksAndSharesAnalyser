from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError, ContentTooShortError
import bs4
import logging
from logger import Logger

class BaseScrapper():
    
    '''Base class used to access webpages using Request'''
    
    def __init__(self, webpage):
        self._logger = Logger(logging.INFO)
        self._log = self._logger.config_logger()
        self._webpage = webpage
        self._soup = self.get_webpage()
        
    def get_webpage(self):
        
        ''' Returns the html of a given webpage'''
        
        try:
            req = Request(self._webpage)
            webpage = urlopen(req, timeout=30).read()
            soup = bs4.BeautifulSoup(webpage, "html.parser")
            
            return soup
        
        except URLError as urlerror:
            self._log.error(urlerror)
            return None
        except HTTPError as httperror:
            self._log.error(httperror)
            return None
        except ContentTooShortError as ctserror:
            self._log.error(ctserror)
            return None
        except Exception as error:
            self._log.error(error)
            return None
            
