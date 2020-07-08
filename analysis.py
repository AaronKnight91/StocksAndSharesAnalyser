from datetime import datetime
import pandas as pd

class AnalyseRatios:

    def __init__(self, outpath, df):

        self._opath = outpath
        self._df = df
        self._today = datetime.now().strftime("%Y%m%d")

        self._cuts = [[15,0.8,10,1,100,10,35],[25,1,15,1.5,150,10,50],[25,1,15,1.5,150,10,65]]
        
        self._new_df = pd.DataFrame()
        
    def analyse(self):

        columns =["Company Name","P/E Ratio","P/S Ratio","Cash Flow","P/B Ratio", "Debt to Equity","Dividend Yield","Payout Ratio"]

        for i in range(len(self._cuts)):
            l = []
            for index, row in self._df.iterrows():
                if row["pe_ratio"] <= self._cuts[i][0] and not row["pe_ratio"] == -999:
                    if row["ps_ratio"] <= self._cuts[i][1] and not row["ps_ratio"] == -999:
                        if row["cash_flow"] <= self._cuts[i][2] and not row["cash_flow"] == -999:
                            if row["pb_ratio"] <= self._cuts[i][3] and not row["pb_ratio"] == -999:
                                if row["debt_to_equity"] <= self._cuts[i][4] and not row["debt_to_equity"] == -999:
                                    if row["dividend_yield"] <= self._cuts[i][5] and not row["dividend_yield"] == -999:
                                        if row["payout_ratio"] <= self._cuts[i][6] and not row["payout_ratio"] == -999:
                                            try:
                                                entry = self._df.loc[index]
                                                data = {"Company Name": entry["Company Name"],
                                                        "P/E Ratio":entry["pe_ratio"],
                                                        "P/S Ratio":entry["ps_ratio"],
                                                        "Cash Flow":entry["cash_flow"],
                                                        "P/B Ratio":entry["pb_ratio"],
                                                        "Debt to Equity":entry["debt_to_equity"],
                                                        "Dividend Yield":entry["dividend_yield"],
                                                        "Payout Ratio":entry["payout_ratio"]}
                                                l.append(data)
                                                self._df.drop(self._df.index[index], inplace=True)
                                            except Exception as error:
                                                print("[ERROR]: Skipping company")
                                                print(error)
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
