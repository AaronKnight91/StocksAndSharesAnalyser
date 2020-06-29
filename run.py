import csv
import time

from company import Company

def run():

    with open("freetrade_uk_shares.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if not row[4] == "Investing.com" and not row[4] == "":
                company = Company(row[4])
                print(company._pe_ratio, "\n")
                time.sleep(1)
  
if __name__ == "__main__":
    run()
