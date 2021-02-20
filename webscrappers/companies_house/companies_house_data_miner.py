import argparse
from datetime import date
import pandas as pd
from time import sleep
import logging

from companies_house_scrapper import GetCompaniesHouse
from logger import Logger

##########################################
# Global Variables
##########################################
# Create a logger
logger = Logger(logging.INFO)
log = logger.config_logger()

# Get today's date for any output
today = date.today().strftime("%Y%m%d")
##########################################

### Need to add a better way of appending data to the excel file

def main(args):
   
    # Load company IDs
    company_ids = load_companies()
    
    # Create array to store data
    company_data = []

    print("# Scrapping data...")
    log.info("Scrapping data")

    # Loop over companies    
    for id_number in company_ids:
        
        # Append 0 to the beginning of the id to match the URL
        if str(id_number)[0].isnumeric():
            id_number = "0" + str(id_number)

        log.info("Scrapping data from %s" % id_number)
        
        # URL layout
        page = "https://find-and-update.company-information.service.gov.uk/company/%s/officers" % id_number

        # Get html from Companies House
        data = GetCompaniesHouse(page)

        # Get data about officers of a company from the GetCompaniesHouse class
        officers = data.get_officers()
        
        # Continue if no data
        if len(officers) == 0:
            continue

        # Append data to the company_data array
        log.info("Appending officers data to company_data array")        
        company_data.append(officers)
        
        sleep(1) # sleep for 1 second to avoid 406 error

    # Create one data frame of all companies after loop is finished
    df = create_df(company_data)

    # Save to excel file    
    df.to_excel("%s/%s_company_officers_data.xlsx" % (args.output_directory, today), index=False)
    
def load_companies():

    '''Load company IDs from file'''
    
    print("# Loading data...")
    log.info("Loading data")
    df = pd.read_excel("C:/Users/Aaron.Knight/Documents/Companies House Scrapper/company_ids.xlsx")

    return df["Companies House ID"]

def create_df(data):
    
    '''Create one dataframe to save to file'''

    print("# Creating Dataframe...")
    log.info("Creating dataframe")

    # Header used in the excel file
    header = ["Company ID", "Company Name", "First Names", 
              "Last Name", "Status", "DOB", "Age", "Role",
               "Appointed On", "Resigned On", "Nationality",
               "Country of Residence", "Occupation"]
    
    # Empty array to append to
    array = []

    # For each officer (j) in each company (i), append to the blank array
    for i in range(len(data)):
        for j in data[i]:
            array.append(j)

    # Create dataframe from the array and header array        
    df = pd.DataFrame(array, columns=header)

    # Return dataframe
    return df

def check_arguments():
    
    parse = argparse.ArgumentParser(description="Scrape data from companies house")
    
    parse.add_argument("--output_directory","-od",type=str,help="Output directory path",default="C:/Users/Aaron.Knight/Documents/Data/Companies House")
    
    args = parse.parse_args()
    return args
    
if __name__ == "__main__":
    args = check_arguments()
    main(args)