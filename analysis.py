from datetime import datetime
import pandas as pd

class AnalyseRatios:

    def __init__(self, outpath, df):

        self._opath = outpath
        self._df = df
        self._today = datetime.now().strftime("%Y%m%d")

        self._new_df = pd.DataFrame()
        
    def analyse(self):

        l = []
        columns =["Company Name","P/E Ratio","P/S Ratio","Cash Flow","P/B Ratio", "Debt to Equity","Dividend Yield","Payout Ratio"]
        for index, row in self._df.iterrows():
            if row["pe_ratio"] <= 15 and row["ps_ratio"] <= 0.8 and row["cash_flow"] <= 10 and row["pb_ratio"] <= 1 and row["debt_to_equity"] <= 100 and row["dividend_yield"] <= 10 and row["payout_ratio"] <= 35:

                entry = self._df.loc[index]
                data = {"Company Name": entry[0],
                        "P/E Ratio":entry[1],
                        "P/S Ratio":entry[2],
                        "Cash Flow":entry[3],
                        "P/B Ratio":entry[4],
                        "Debt to Equity":entry[5],
                        "Dividend Yield":entry[6],
                        "Payout Ratio":entry[7]}
                l.append(data)
                self._df.drop(self._df.index[index], inplace=True)
        self._new_df = pd.DataFrame(l, columns = columns)

    def save_output(self):
        self._new_df.to_csv("%s/analysis/%s_analysed_companies.csv" % (self._opath,self._today))

        
    def analyse_pe_ratio(self, lower_limit=0, upper_limit=15):
        if lower_limit == 0:
            self._df.drop(self._df[self._df.pe_ratio < lower_limit].index, inplace=True)
        else:
            self._df.drop(self._df[self._df.pe_ratio <= lower_limit].index, inplace=True)
        self._df.drop(self._df[self._df.pe_ratio > upper_limit].index, inplace=True)

    def analyse_ps_ratio(self, ratio):
        self._df.drop(self._df[self._df.ps_ratio > ratio].index,inplace=True)
        self._df.drop(self._df[self._df.ps_ratio < 0].index,inplace=True)

    def analyse_cash_flow(self, ratio):
        self._df.drop(self._df[self._df.cash_flow > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.cash_flow < 0].index, inplace=True)

    def analyse_pb_ratio(self, ratio):
        self._df.drop(self._df[self._df.pb_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.pb_ratio <= 0].index, inplace=True)

    def analyse_debt_to_equity(self, ratio):
        self._df.drop(self._df[self._df.debt_to_equity > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.debt_to_equity <= 0].index, inplace=True)
        
    def analyse_dividend_yield(self, ratio):
        #self._df.drop(self._df[self._df.dividend_yield > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.dividend_yield < 0].index, inplace=True)

    def analyse_payout_ratio(self, ratio):
        self._df.drop(self._df[self._df.payout_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.payout_ratio < 0].index, inplace=True)

    def save_to_csv(self):
        self._df.to_csv("%s/analysis/%s_analysed_companies.csv" % (self._opath,self._today))
        
    def append_to_csv(self):
        self._df.to_csv("%s/analysis/%s_analysed_companies.csv" % (self._opath,self._today), mode="a", header=False)
