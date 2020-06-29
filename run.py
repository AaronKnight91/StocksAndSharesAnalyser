import csv
import time

from company import Company
from company_database import CompanyDatabase

def run():

    with open("freetrade_uk_shares.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            if not row[4] == "":
                print(type(row[0]), row[0])
                company = Company(row[4])
                print(str(row[0]))
                cdb = CompanyDatabase("companies.db",str(row[0]))
                print("DEBUG")
                cdb.insert("TODAY",
                           float(company._pe_ratio),
                           float(company._ps_ratio),
                           float(company._cash_flow),
                           float(company._pb_ratio),
                           float(company._dividend_yield),
                           float(company._payout_ratio))
                cdb.__del__()
                time.sleep(1)
            else:
                continue
  
if __name__ == "__main__":
    run()
