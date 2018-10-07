'''
    Craw script for abs.com
    Source file: import_data.csv
    Output directory: out/
    @Author Bai
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
source_data = "RealEsate/import_data.csv"
simple_data_link = "http://quickstats.censusdata.abs.gov.au/census_services/getproduct/census/2016/quickstat/POA{}?opendocument"
# profile_link = "http://quickstats.censusdata.abs.gov.au/census_services/getproduct/census/2016/communityprofile/POA{}?opendocument"

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = { 'User-Agent' : user_agent}


if __name__ == "__main__":
    import_area = pd.read_csv(source_data)
    for postcode in import_area['Postcode']:
        if postcode == 2134:
            r = requests.get(simple_data_link.format(postcode))
            soup = BeautifulSoup(r.text,"xml")
            print(soup.find("peopleContent"))
