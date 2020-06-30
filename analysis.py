import pandas as pd

class AnalyseRatios:

    def __init__(self, df):
        self._df = df

    def analyse_pe_ratio(self, ratio):
        self._df = self._df.drop(df[df.pe_ratio < ratio].index)

    def analyse_ps_ratio(self, ratio):
        self._df = self._df.drop(df[df.ps_ratio < ratio].index)

    def analyse_cash_flowo(self, ratio):
        self._df = self._df.drop(df[df.cash_flow < ratio].index)

    def analyse_pb_ratio(self, ratio):
        self._df = self._df.drop(df[df.pb_ratio < ratio].index)

    def analyse_dividend_yield(self, ratio):
        self._df = self._df.drop(df[df.dividend_yield < ratio].index)

    def analyse_payout_ratio(self, ratio):
        self._df = self._df.drop(df[df.payout_ratio < ratio].index)

