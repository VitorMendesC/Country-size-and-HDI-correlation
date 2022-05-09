import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import re
import os

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)   # script runs only on the first run, performance isn't an issue
CSV_NAME = "country_hdi_land.csv"

def generate_CSV():
    PAGE_COUNTRY_BY_SIZE = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area")
    PAGE_COUNTRY_BY_HDI = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index")

    COUNTRY_BY_SIZE_SOUP = BeautifulSoup(PAGE_COUNTRY_BY_SIZE.text, 'html.parser')
    COUNTRY_BY_HDI_SOUP = BeautifulSoup(PAGE_COUNTRY_BY_HDI.text, 'html.parser')

    hdi_table = pd.read_html(str(COUNTRY_BY_HDI_SOUP.find('table',{'class':"wikitable"})))
    hdi_table = pd.DataFrame(hdi_table[0])
    hdi_table = hdi_table.drop("Rank", axis=1)
    hdi_table.columns = hdi_table.columns.droplevel()
    hdi_table = hdi_table.drop("Average annual growth (2010–2019)​[18]", axis=1)
    hdi_table = hdi_table.rename(columns={"2019 data (2020 report)​[2]":"HDI", "Country/Region":"Country"})

    size_table = pd.read_html(str(COUNTRY_BY_SIZE_SOUP.find('table',{'class':"wikitable"})))
    size_table = pd.DataFrame(size_table[0])
    size_table = size_table.drop(["Rank","Total in km2 (mi2)", "Water in km2 (mi2)", "% water", "Notes"], axis=1)
    size_table = size_table.rename(columns={"Country / Dependency":"Country", "Land in km2 (mi2)":"Land"})

    # Data cleaning
    for index, row in size_table.iterrows():
        row[0] = re.sub("[\(\[].*?[\)\]]", "", row[0])              # remove anything between parenthesis in country name

        while row[0][0] == ' ':                                     # remove leading spaces in country name 
            row[0] = row[0][1:]
        while row[0][-1] == ' ':                                    # remove trailing spaces in country name
            row[0] = row[0][:-1]

        row[1] = re.sub("[\(\[].*?[\)\]]", "", str(row[1]))         # remove anything between parenthesis in country land size

        for index, value in enumerate(row[1]):                      # for some reason USA has 2 values for land separated by '-', this gets the first value
            if value == '–' or value == '.':                        # and also removes the decimal part 
                row[1] = row[1][:index]

        row[1] = row[1].replace(",","")
        row[1] = row[1].replace(" ","")
        

    final_table = pd.merge(hdi_table, size_table, how="left", on=["Country"])
    final_table = final_table.dropna()
    final_table = final_table[final_table['Land'] != 'nan']         # there is some strings 'nan' that dropna() doesn't drop

    final_table.to_csv(os.path.join(os.getcwd(), CSV_NAME), index = False)
    return