import sqlite3

class OwnedStocks:

    """
    This class allows the user to track a company that they own.
    The date they bought the company, the number of shares and at what price.
    This will allow the average price to be tracked and alerts sent out when the price drops by 25%.
    """

    def __init__(self, company, table="purchases", trigger_level = -0.25):
        # Initilize class attributes
        self._company = company
        self._company = self.string_converter()
        self._table = table
        self._trigger_level = trigger_level

        # Initilize sqlite3 database
        self._conn = sqlite3.connect("data/owned/%s.db" % self._company)
        self._cur = self._conn.cursor()
        if self._table == "purchases":
            self._cur.execute("CREATE TABLE IF NOT EXISTS purchases (id INTEGER PRIMARY KEY, date TEXT, num_shares REAL, price REAL, total_cost REAL, average_price REAL)")
        elif self._table == "dividend":
            self._cur.execute("CREATE TABLE IF NOT EXISTS dividends (id INTEGER PRIMARY KEY, date TEXT, dividend_per_share REAL, total_dividend REAL)")
        self._conn.commit()

        self._new_purchase = ()
        self._new_dividend = ()
        self._data = self.view()
        self._average_price = self.calc_average_price()
        self._total_dividend = self.calc_total_dividend()

    def get_new_purchase(self, date, num_shares, price, total_cost):
        self._new_purchase = (0, date, num_shares, price, total_cost)

    def get_new_dividend(self, date, dividend_per_share, total_dividend):
        self._new_dividend(0, date dividend_per_share, total_dividend)
        
    def insert_purchases(self, date, num_shares, price, total_cost):
        self._cur.execute("INSERT INTO purchases VALUES (NULL, ?, ?, ?, ?, ?)", (date, num_shares, price, total_cost, self._average_price))
        self._conn.commit()

    def insert_dividends(self, date, dividend_per_share, total_dividend):
        self._cur.execute("INSERT INTO dividends VALUES (NULL, ?, ?, ?)", (date, dividend_per_share, total_dividend))
        self._conn.commit()

    def view(self):
        self._cur.execute("SELECT * FROM %s" % self._table)
        rows =self._cur.fetchall()
        return rows
    
    def delete(self, id):
        self._cur.execute("DELETE FROM %s WHERE id=?" % self._table,(id,))
        self._conn.commit()

    def __del__(self):
        self._conn.close()

    def calc_average_price(self):

        numerator = 0
        tot_num_shares = 0
        for i in range(len(self._data)):
            numerator +=  self._data[i][2] * self._data[i][3] # num_shares * price
            tot_num_shares += self._data[i][2] # num_shares

        if len(self._new_purchase) > 0:
            numerator += self._new_purchase[2] * self._new_purchase[3]
            tot_num_shares += self._new_purchase[2]

        try:
            weighted_average_price = numerator / tot_num_shares
        except Exception as error:
            print(error)

        self._average_price = weighted_average_price

    def calc_total_dividend(self):

        tot = 0
        for i in range(len(self._data)):
            tot += self._data[3]

        if len(self._new_dividend) > 0:
            tot += self._new_dividend[3]

        self._total_dividend = tot
        
        
    def trigger(self, current_price):

        percentage_change = (current_price - self._average_price) / self._average_price
        if percentage_change <= self._trigger_level:
            return True
        else:
            return False


    def string_converter(self):

        d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

        output_string = ""
        for character in self._company:
            if character.isnumeric():
                output_string += d[int(character)]
            elif not character.isalnum():
                continue
            else:
                output_string += character

        return output_string.lower()
