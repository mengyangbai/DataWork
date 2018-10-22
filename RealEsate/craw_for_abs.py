# -*- coding: utf-8 -*-
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

'''
var maritalStatusData = [];
var ancestryParagraphs = [];
var ancestryData = [];
var religiousAffiliationParagraphs = [];
var religiousAffiliationData = [];
var languageParagraphs = [];
var languageData = [];
var occupationParagraphs = [];
var occupationData = [];
var countryOfBirthParagraphs = [];
var countryOfBirthData = [];
var travelToWorkParagraphs = [];
var travelToWorkData = [];
var industryParagraphs = [];
var industryData = [];
var countryOfFatherParagraphs = [];
var countryOfFatherData = [];
var countryOfMotherParagraphs = [];
var countryOfMotherData = [];
'''
# Direct read the js data, is the fastest solution


# Direct crawling

if __name__ == "__main__":
    import_area = pd.read_csv(source_data)
    for postcode in import_area['Postcode']:
        if postcode == 2134:
            r = requests.get(simple_data_link.format(postcode))
            soup = BeautifulSoup(r.text,features="lxml")
            # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
            for sibling in soup.find(id="peopleContent").table.next_siblings:
                # if sibling.string and "<!-- People -->" in sibling.string:
                if sibling and sibling.table:
                    print(sibling)
                    print("---------")
            # print(soup.find_all(id="countryOfBirthTable"))