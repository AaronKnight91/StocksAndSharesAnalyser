import csv
import time
from datetime import datetime

from company import Company
from company_database import CompanyDatabase

def run():

    today = datetime.now().strftime("%Y%m%d")

    with open("freetrade_uk_shares.csv","r",encoding='cp1252') as csv_file:
        reader = csv.reader(csv_file)

        l = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[5] == "":
                continue

            print("Scrapping data for %s" % row[0])

            #d = {}
            company = Company(row[5])
            #d = {"pe_ratio":company._pe_ratio,
            #     "ps_ratio":company._ps_ratio,
            #     "cash_flow":company._cash_flow,
            #     "pb_ratio":company._pb_ratio,
            #     "dividend_yield":company._dividend_yield,
            #     "payout_ratio":company._payout_ratio}
              
            cdb = CompanyDatabase("companies.db",str(row[1]).replace("-","").replace("&","").replace("'",""))
            cdb.insert(today,
                       float(company._pe_ratio),
                       float(company._ps_ratio),
                       float(company._cash_flow),
                       float(company._pb_ratio),
                       float(company._dividend_yield),
                       float(company._payout_ratio))
            cdb.__del__()
            time.sleep(1)
           
        #for i in l:
        #    print(i)
            
if __name__ == "__main__":
    run()
