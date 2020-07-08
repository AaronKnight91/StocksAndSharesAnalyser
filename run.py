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
                company = Company(row[5])
                if not args.noanalysis:
                    d = {}
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
                           float(company._free_cash_flow),
                           float(company._pb_ratio),
                           float(company._tangible_pb_ratio),
                           float(company._gross_margin_ttm),
                           float(company._gross_margin_5ya),
                           float(company._operating_margin_ttm),
                           float(company._operating_margin_5ya),
                           float(company._pretax_margin_ttm),
                           float(company._pretax_margin_5ya),
                           float(company._net_profit_margin_ttm),
                           float(company._net_profit_margin_5ya),
                           float(company._revenue_per_share),
                           float(company._basic_eps),
                           float(company._diluted_eps),
                           float(company._book_value_per_share),
                           float(company._tangible_book_value_per_share),
                           float(company._cash_per_share),
                           float(company._cash_flow_per_share),
                           float(company._return_on_equity_ttm),
                           float(company._return_on_equity_5ya),
                           float(company._return_on_assets_ttm),
                           float(company._return_on_assets_5ya),
                           float(company._return_on_investment_ttm),
                           float(company._return_on_investment_5ya),
                           float(company._eps_mrq_vs_mrq_1yr_ago),
                           float(company._eps_ttm_vs_ttm_1yr_ago),
                           float(company._eps_growth_5ya),
                           float(company._sale_mrq_vs_qtr_1ya_ago),
                           float(company._sale_ttm_vs_ttm_1ya_ago),
                           float(company._sales_growth_5ya),
                           float(company._capital_spending_growth_5ya),
                           float(company._quick_ratio),
                           float(company._current_ratio),
                           float(company._lt_debt_to_equity),
                           float(company._total_debt_to_equity),
                           float(company._asset_turnover),
                           float(company._inventory_turnover),
                           float(company._revenue_per_employee),
                           float(company._net_income_per_employee),
                           float(company._receivable_turnover),
                           float(company._dividend_yield),
                           float(company._dividend_yield_5ya),
                           float(company._dividend_growth_rate),
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
