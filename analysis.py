import pandas as pd

class AnalyseRatios:

    def __init__(self, df):
        self._df = df

    def analyse_pe_ratio(self, ratio):
        self._df.drop(self._df[self._df.pe_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.pe_ratio < 0].index, inplace=True)

    def analyse_ps_ratio(self, ratio):
        self._df.drop(self._df[self._df.ps_ratio > ratio].index,inplace=True)
        self._df.drop(self._df[self._df.ps_ratio < 0].index,inplace=True)

    def analyse_cash_flow(self, ratio):
        self._df.drop(self._df[self._df.cash_flow > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.cash_flow < 0].index, inplace=True)

    def analyse_pb_ratio(self, ratio):
        self._df.drop(self._df[self._df.pb_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.pb_ratio <= 0].index, inplace=True)

    def analyse_dividend_yield(self, ratio):
        #self._df.drop(self._df[self._df.dividend_yield > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.dividend_yield < 0].index, inplace=True)

    def analyse_payout_ratio(self, ratio):
        self._df.drop(self._df[self._df.payout_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.payout_ratio < 0].index, inplace=True)

    def save_to_csv(self):
        self._df.to_csv("analysed_companies.csv")
