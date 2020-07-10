import sqlite3

class OwnedStocks:

    """
    This class allows the user to track a company that they own.
    The date they bought the company, the number of shares and at what price.
    This will allow the average price to be tracked and alerts sent out when the price drops by 25%.
    """

    def __init__(self, company, trigger_level = -0.25):#, date, num_shares, price, total_cost, trigger_level = -0.25):
        self._company = company
        self._company = self.string_converter()
        #self._data = date
        #self._num_shares = num_shares
        #self._price = price

        self._conn = sqlite3.connect("data/owned/%s.db" % self._company)
        self._cur = self._conn.cursor()
        self._cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, date TEXT, num_shares REAL, price REAL, total_cost REAL)" % self._)
        self._conn.commit()

        self._trigger_level = trigger_level
        
        self._data = self.view()
        print(self._data)
        self._average_price = self.calc_average_price()
        print(self._average_price)

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

    def insert(self, date, num_shares, price, total_cost):
        self._cur.execute("INSERT INTO %s VALUES (NULL, ?, ?, ?, ?)" % self._company, (date, num_shares, price, total_cost))
        self._conn.commit()

    def view(self):
        self._cur.execute("SELECT * FROM %s" % self._company)
        rows =self._cur.fetchall()
        print(rows)
        return rows
    
    def calc_average_price(self):#num_shares, price):

        if not len(self._data) > 0:
            return 0

        print(self._data[1][1])
        numerator = 0
        tot_num_shares = 10
        for i in range(len(self._data)):
            print(self._data[i][1])
            #numerator +=  self._data[i][1] * self._data[i][2] # num_shares * price
            #tot_num_shares += self._data[i][1] # num_shares
            
        weighted_average_price = numerator / tot_num_shares

        return weighted_average_price

    def update_ave_price(self):
        self._average_price = self.calc_average_price()
        
    def trigger(self, current_price):

        percentage_change = (current_price - self._average_price) / self._average_price
        if percentage_change <= self._trigger_level:
            return True
        else:
            return False

