import argparse
import csv
import time
from datetime import datetime
import pandas as pd

from company import Company
from company_database import CompanyDatabase
from analysis import AnalyseRatios

def run(args):

    today = datetime.now().strftime("%Y%m%d")

    l = []
    with open("%s/inputs/freetrade_uk_shares.csv" % args.data,"r",encoding='cp1252') as csv_file:
        reader = csv.reader(csv_file)

        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[5] == "":
                continue

            #if i == 50: break

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
              
                cdb = CompanyDatabase("%s/databases/companies.db" % args.data,str(row[1]).replace("-","").replace("&","").replace("'",""))
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

    if not args.noanalysis:
        
        df = pd.DataFrame(l)

        print("# Analysing results...")
        analysis = AnalyseRatios(args.data,df)
        analysis.analyse()
        analysis.save_output()

def check_arguments():

    parser = argparse.ArgumentParser(description="Arguments for the Investment App")

    parser.add_argument("--noanalysis","-na",action="store_true",help="This argument will run the programme without analysising the data")

    parser.add_argument("--data","-d",type=str,help="The path that any data will be read from/to will be saved to",default="data")
    
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    args = check_arguments()
    run(args)
