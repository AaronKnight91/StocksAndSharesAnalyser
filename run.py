import csv
import time
from datetime import datetime
import pandas as pd

from company import Company
from company_database import CompanyDatabase

def run():

    today = datetime.now().strftime("%Y%m%d")

    l = []
    with open("freetrade_uk_shares.csv","r",encoding='cp1252') as csv_file:
        reader = csv.reader(csv_file)

        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[5] == "":
                continue

            print("Scrapping data for %s" % row[0])

            d = {}
            company = Company(row[5])
            d = {"Company Name": row[0],
                 "pe_ratio":company._pe_ratio,
                 "ps_ratio":company._ps_ratio,
                 "cash_flow":company._cash_flow,
                 "pb_ratio":company._pb_ratio,
                 "dividend_yield":company._dividend_yield,
                 "payout_ratio":company._payout_ratio}
            l.append(d)
              
            cdb = CompanyDatabase("companies.db",str(row[1]).replace("-","").replace("&","").replace("'",""))
            cdb.insert(today,
                       float(company._pe_ratio),
                       float(company._ps_ratio),
                       float(company._cash_flow),
                       float(company._pb_ratio),
                       float(company._dividend_yield),
                       float(company._payout_ratio))
            cdb.__del__()
            time.sleep(1) # Make programme sleep for 1 second

    df = pd.DataFrame(l)
    print(df)

    results = analyse_results(df)
    print(results)
    
def analyse_results(df):

    df_copy = df # Make a copy of the DataFrame
    df_copy = df_copy.drop(df[df.pe_ratio > 15].index)
    df_copy = df_copy.drop(df[df.ps_ratio > 0.8].index)
    df_copy = df_copy.drop(df[df.cash_flow > 10].index)
    df_copy = df_copy.drop(df[df.pb_ratio < 1].index)
    df_copy = df_copy.drop(df[df.payout_ratio < 35].index)

    return df_copy
    
if __name__ == "__main__":
    run()
