#!/usr/bin/env python3

import argparse
import csv
import time
from datetime import datetime
import pandas as pd
import os

from company import Company
from company_database import CompanyDatabase
from analysis import AnalyseRatios
from stock_tracker import OwnedStocks

def run(args):

    today = datetime.now().strftime("%Y%m%d")
    l = []

    if not args.noscrapping:
        scrape_data(today,l)
    
    if not args.noanalysis or not args.noscrapping:
        run_analysis(l)

    if args.stocktracker == "purchases":
        while True:
            company = input("Please enter the name of the company you have bought: ")
            date = input("Please enter the date you bought the shares using the YYYY/MM/DD format: ")
            portfolio = input("What portfolio is the company part of? ")
            num_shares = input("Please enter the number of shares you bought: ")
            price = input("Please enter the price at which you bought the shares: ")
            total_cost = input("Please enter the total cost of the transaction: ")

            share = OwnedStocks(str(company))#, trigger_level = -0.25)
            share.get_new_purchase(str(date), str(portfolio), float(num_shares), float(price), float(total_cost))
            share.calc_average_price()
            share.insert_purchases(str(date), str(portfolio), float(num_shares), float(price), float(total_cost))

            q = input("Do you want to add another purchase (Y/N)?: ")
            if str(q).upper() == "N":
                break
            
    elif args.stocktracker == "dividends":
        while True:
            company = input("Please enter the name of the company you have bought: ")
            date = input("Please enter the date you were paid this dividend using the YYYY/MM/DD format: ")
            portfolio = input("What portfolio is the company part of? ")
            div_type = input("What type of dividend is this? ")
            dividend_per_share = input("Please enter the vale of the dividend per share: ")
            total_dividend = input("Please enter the value of the total dividend payment: ")

            share = OwnedStocks(str(company), table="dividends")
            share.get_new_dividend(str(date), str(portfolio), str(div_type), float(dividend_per_share), float(total_dividend))
            share.insert_dividend(str(date), str(portfolio), str(div_type), float(dividend_per_share), float(total_dividend))
            share.calc_total_dividend()

            print("Total Dividend to date: ", share._total_dividend)

            q = input("Do you want to add another dividend payment (Y/N)?: ")
            if str(q).upper() == "N":
                break
        
def scrape_data(today, l):

    df = pd.read_csv(os.path.abspath("%s/%s" % (args.input, args.indata)), encoding = "ISO-8859-1")
    
    loops = 0
    length = len(df)
    while length > 0 or loops < 10:
        length = len(df)
        for index, row in df.iterrows():
            print("# Scrapping data for %s" % row["Company Name"])

            sql_table_name = string_converter(row["Company Name"])

            try:
                if row["Investing.com"] == "None":
                    df.drop(index, inplace=True)
                    continue
                company = Company(row["Investing.com"])
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
                    
                    cdb = CompanyDatabase(os.path.abspath("%s/%s" % (args.databases,args.savedatabase)), sql_table_name)
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
                    df.drop(index, inplace=True)
            except Exception as error:                                                                                                               
                print("[ERROR]: Moving on to next company. This company will be attempted again later.")

            loops += 1
            time.sleep(2) # Make programme sleep for 1 second
                    
def string_converter(input_string):

    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

    output_string = ""
    for character in input_string:
        if character.isnumeric():
            output_string += d[int(character)]
        elif not character.isalnum():
            continue
        else:
            output_string += character

    return output_string.lower()        
        
def run_analysis(data):
    
    df = pd.DataFrame(data)
    
    print("# Analysing results...")
    analysis = AnalyseRatios(args.analysis,df)
    analysis.analyse()
    analysis.save_output()

def check_arguments():

    parser = argparse.ArgumentParser(description="Arguments for the Investment App")

    parser.add_argument("--noscrapping","-ns",action="store_true",help="This argument will run the programme without scrapping data. Also, the analysis will not run.")
    parser.add_argument("--stocktracker","-st",type=str,help="This allows the user to enter purchases or dividends into a sql table",choices=["None","purchases","dividends"],default="None")
    parser.add_argument("--noanalysis","-na",action="store_true",help="This argument will run the programme without analysising the data")

    #parser.add_argument("--data","-d",type=str,help="The path that any data will be read from/to will be saved to",default="data")
    parser.add_argument("--input","-i",type=str,help="The path where your input files are saved",default="/home/aaron/investment_app/data/inputs")
    parser.add_argument("--databases","-db",type=str,help="The path where your databases will be stored",default="/home/aaron/investment_app/data/databases")
    parser.add_argument("--analysis","-a", type=str,help="The path where the analysed csv files will be saved",default="/home/aaron/investment_app/data/analysis")

    parser.add_argument("--indata","-id",type=str,help="The csv file that will be used to get the data from",default="freetrade_uk_shares.csv")
    parser.add_argument("--savedatabase","-sb",type=str,help="The database in which company data will be saved",default="companies.db")
    
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    args = check_arguments()
    run(args)
