import sqlite3

class CompanyDatabase:

    def __init__(self, db, table):
        self._table = table.replace(" ", "")
        self._conn = sqlite3.connect(db)
        self._cur = self._conn.cursor()
        self._cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, date TEXT, pe_ratio REAL, ps_ratio REAL, cash_flow REAL, pb_ratio REAL, dividend_yield REAL, payout_ratio REAL)" % self._table)
        self._conn.commit()

    def insert(self, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("INSERT INTO %s VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)" % self._table,
                          (date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio))
        self._conn.commit()

    def view(self):
        self._cur.execute("SELECT * FROM %s" % self._table)
        rows = self._cur.fetchall()
        return rows

    def search(self, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("SELECT * FROM %s WHERE pe_ratio=? OR ps_ratio=? OR cash_flow=? OR pb_ratio=? OR dividend_yield OR payout_ratio=?" % self._table, (pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio))
        rows = self._cur.fetchall()
        return rows

    def update(self, id, date, pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio):
        self._cur.execute("UPDATE %s SET pe_ratio=?, ps_ratio=?, cash_flow=?, pb_ratio=?, dividend_yield=?, payout_ratio=? WHERE id=?" % self._table,
                         (pe_ratio, ps_ratio, cash_flow, pb_ratio, dividend_yield, payout_ratio,id))
        self._conn.commit()

    def delete(self, id):
        self._cur.execute("DELETE FROM %s WHERE id=?" % self._table,(id,))
        self._conn.commit()

    def __del__(self):
        self._conn.close()
