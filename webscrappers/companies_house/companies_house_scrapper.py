import bs4
import re
from datetime import date
import logging
from base_scrapper import BaseScrapper
from logger import Logger

class GetCompaniesHouse(BaseScrapper):
    
    '''Scrape data from the Companies House website
       Create an 'officer' for every member of the company listed
       
       This class inherits from the BaseScrapper class'''
    
    def __init__(self, webpage):
        
        BaseScrapper.__init__(self, webpage)
        self._officers = []

        self._logger = Logger(logging.INFO)
        self._log = self._logger.config_logger()

        try:

            self._company_name = self.get_company_name(self._soup)
            self._company_number = self.get_company_number(self._soup)
    
            self._html = self._soup.find_all("div")
            
            for i in self._html:
                appointment = []
                            
                if i.has_attr("class") and "appointment-" in i["class"][0]:
                    self._name = self.get_name(i)
                    self._first_name, self._last_name = self.separate_names()
                    
                    self._status = self.get_status(i)
                    self._role = self.get_role(i)
                    self._dob = self.get_dob(i)
                    self._age = self.calculate_age()
                    self._date_appointed = self.get_date_appointed(i)
                    self._date_resigned = self.get_date_resigned(i)
                    self._nationality = self.get_nationality(i)
                    self._country_of_residence = self.get_cor(i)
                    self._occupation = self.get_occupation(i)
                    
                    appointment.append(self._company_number)
                    appointment.append(self._company_name)
                    appointment.append(self._first_name)
                    appointment.append(self._last_name)
                    appointment.append(self._status)
                    appointment.append(self._dob)
                    appointment.append(self._age)
                    appointment.append(self._role) 
                    appointment.append(self._date_appointed)
                    appointment.append(self._date_resigned)
                    appointment.append(self._nationality) 
                    appointment.append(self._country_of_residence)
                    appointment.append(self._occupation)
                    
                    self._officers.append(appointment)
                                        
        except Exception as error:
            self._log.error(error)
            
    def get_officers(self):
        return self._officers

    def get_company_name(self, soup):

        try:
            company_name = soup.findAll("p",{"class":"heading-xlarge"})
            return company_name[0].text.strip()
        except:
            return ""
        
    def get_company_number(self, soup):

        try:
            company_number = soup.find("p",{"id":"company-number"})
            return company_number.text.split()[-1]
        except:
            return ""

    def get_name(self, appointment):
        
        try:
            return appointment.find("a").text.strip()
        except:
            return ""
    
    def separate_names(self):

        try:
            name = self._name.split(",")
            
            if len(name) < 2:
                
                return name[0], ""
            
            else:
            
                first_names = name[1].strip()
                last_name = name[0].strip()
            
                return first_names, last_name
        except:
            return self._name
        
    def get_status(self, appointment):

        try:
            a = appointment.find("div", {"class":"grid-row"}) 
            for i in a:
                if isinstance(i.find("span"), bs4.element.Tag):
    
                    return i.find("span").text.strip()
        except:
            return ""
            
    def get_role(self, appointment):

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                role = i.findAll("dd",id=re.compile(".role."))
                if len(role) > 0:
                    return role[0].text.strip()
        except:
            return ""
            
    def get_dob(self, appointment):          

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                dob = i.findAll("dd",id=re.compile(".date-of-birth."))
                if len(dob) > 0:
                    return dob[0].text.strip()
        except:
            return ""
        
    def calculate_age(self):

        try:        
            if self._dob == None:
                return None
           
            dob = self._dob.split()        
            today = date.today()
            months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
                      "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
    
            age = today.year - int(dob[1]) - (today.month < months[dob[0]])
    
            return age
        except:
            return -1

    def get_date_appointed(self, appointment):          

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                date = i.findAll("dd",id=re.compile("officer-appointed-on-."))
                if len(date) > 0:
                    return date[0].text.strip()
        except:
            return ""

    def get_date_resigned(self, appointment):

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                date = i.findAll("dd",id=re.compile("officer-resigned-on."))
                if len(date) > 0:
                    return date[0].text.strip()
        except:
            return ""
            
    def get_nationality(self, appointment):          

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                nationality = i.findAll("dd",id=re.compile("officer-nationality."))
                if len(nationality) > 0:
                    return nationality[0].text.strip()
        except:
            return ""
        
    def get_cor(self, appointment):          

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                cor = i.findAll("dd",id=re.compile("officer-country-of-residence."))
                if len(cor) > 0:
                    return cor[0].text.strip()
        except:
            return ""

    def get_occupation(self, appointment):          

        try:
            a = appointment.findAll("div", {"class":"grid-row"})
            for i in a:
                occupation = i.findAll("dd",id=re.compile("officer-occupation."))
                if len(occupation) > 0:
                    return occupation[0].text.strip()
        except:
            return ""
