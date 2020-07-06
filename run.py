import csv
import time
from datetime import datetime
import pandas as pd

from company import Company
from company_database import CompanyDatabase
from analysis import AnalyseRatios

def run():

    today = datetime.now().strftime("%Y%m%d")

    l = []
    with open("data/freetrade_uk_shares.csv","r",encoding='cp1252') as csv_file:
        reader = csv.reader(csv_file)

        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[5] == "":
                continue

            print("Scrapping data for %s, %s" % (row[0], row[2]))
            try:
                d = {}
                company = Company(row[5])
                d = {"Company Name": row[0],
                     "pe_ratio":company._pe_ratio,
                     "ps_ratio":company._ps_ratio,
                     "cash_flow":company._cash_flow,
                     "pb_ratio":company._pb_ratio,
                     "debt_to_equity":company._total_debt_to_equity,
                     "dividend_yield":company._dividend_yield,
                     "payout_ratio":company._payout_ratio}
                l.append(d)
              
                cdb = CompanyDatabase("data/companies.db",str(row[1]).replace("-","").replace("&","").replace("'",""))
                cdb.insert(today,
                           float(company._pe_ratio),
                           float(company._ps_ratio),
                           float(company._cash_flow),
                           float(company._pb_ratio),
                           float(company._dividend_yield),
                           float(company._payout_ratio))
                
                cdb.remove_duplicate_rows()

                cdb.__del__()
                time.sleep(1) # Make programme sleep for 1 second
            except Exception as error:
                print("[ERROR]: Skipping company")
                print(error)
                
    df = pd.DataFrame(l)
    df_copy = df.copy()

    print("# Analysing results...")
    results = analyse_results(df_copy)

    analysis = AnalyseRatios(df)
    analysis.analyse_pe_ratio(0.0,30.0)
    analysis.analyse_ps_ratio(1.0)
    analysis.analyse_cash_flow(15.0)
    analysis.analyse_pb_ratio(1.5)
    analysis.analyse_debt_to_equity(150)
    analysis.analyse_dividend_yield(20)
    analysis.analyse_payout_ratio(50)

    analysis.append_to_csv()

    new_df = pd.read_csv("data/%s_analysed_companies.csv" % today)
    df.drop_duplicates(inplace=True)
    df.to_csv("data/%s_analysed_companies.csv" % today, index=False)
    
def analyse_results(df):

    analysis = AnalyseRatios(df)
    analysis.analyse_pe_ratio(0.0,15.0)
    analysis.analyse_ps_ratio(0.8)
    analysis.analyse_cash_flow(10.0)
    analysis.analyse_pb_ratio(1.0)
    analysis.analyse_debt_to_equity(150)
    analysis.analyse_dividend_yield(20)
    analysis.analyse_payout_ratio(50)

    analysis.save_to_csv()
    
    return analysis._df
    
#    df_copy = df # Make a copy of the DataFrame
#    df_copy = df_copy.drop(df[df.pe_ratio > 15].index)
#    df_copy = df_copy.drop(df[df.ps_ratio > 0.8].index)
#    df_copy = df_copy.drop(df[df.cash_flow > 10].index)
#    df_copy = df_copy.drop(df[df.pb_ratio < 1].index)
#    df_copy = df_copy.drop(df[df.payout_ratio < 35].index)

    return df_copy
    
if __name__ == "__main__":
    run()
