from datetime import datetime
import argparse
import pandas as pd


def main(args):

    df = pd.read_csv("%s/%s" % (args.path, args.file))
    print(df.head())
    
    
def check_args(today):

    parser = argparse.ArgumentParser(description='Open analysis files.')

    parser.add_argument("--path","-p",type=str,help="The directory in which your csv is saved",default="/home/aaron/investment_app/data/analysis")
    parser.add_argument("--file","-f",type=str,help="The csv you wish to read into a data frame",default="%s_analysed_companies.csv" % today)

    args = parser.parse_args()

    return args
        
if __name__ == "__main__":
    today = datetime.today().strftime('%Y%m%d')
    args = check_args(today)
    main(args)
