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

    if not args.noscrapping:
        l, skipped = scrape_data(today, l)
        
    
    if not args.noanalysis or not args.noscrapping:
        run_analysis(l)

def scrape_data(today, l):
    
    with open("%s/%s" % (args.input, args.indata),"r",encoding='cp1252') as csv_file:
        reader = csv.reader(csv_file)

        skipped = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[5] == "":
                continue

            print("Scrapping data for %s, %s" % (row[0], row[2]))
            try:
                company = Company(row[5])
                if company._html == None:
                    print("# Error: skipping %s" % row[0])
                    skipped.append(row[0])
                    continue
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
              
                cdb = CompanyDatabase("%s/%s" % (args.databases,args.savedatabase),str(row[1]).replace("-","").replace("&","").replace("'",""))
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
        return l, skipped
    else:
        return None

def run_analysis(data):        
    df = pd.DataFrame(data)
    
    print("# Analysing results...")
    analysis = AnalyseRatios(args.analysis,df)
    analysis.analyse()
    analysis.save_output()

def check_arguments():

    parser = argparse.ArgumentParser(description="Arguments for the Investment App")

    parser.add_argument("--noscrapping","-ns",action="store_true",help="This argument will run the programme without scrapping data. Also, the analysis will not run.")
    parser.add_argument("--noanalysis","-na",action="store_true",help="This argument will run the programme without analysising the data")

    #parser.add_argument("--data","-d",type=str,help="The path that any data will be read from/to will be saved to",default="data")
    parser.add_argument("--input","-i",type=str,help="The path where your input files are saved",default="./data/inputs")
    parser.add_argument("--databases","-db",type=str,help="The path where your databases will be stored",default="./data/databases")
    parser.add_argument("--analysis","-a", type=str,help="The path where the analysed csv files will be saved",default="./data/analysis")

    parser.add_argument("--indata","-id",type=str,help="The csv file that will be used to get the data from",default="freetrade_uk_shares.csv")
    parser.add_argument("--savedatabase","-sb",type=str,help="The database in which company data will be saved",default="companies.db")
    
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    args = check_arguments()
    run(args)
