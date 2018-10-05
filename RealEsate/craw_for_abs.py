'''
    Craw script for abs.com
    Source file: import_data.csv
    Output directory: out/
    @Author Bai
'''
import pandas as pd

source_data = "RealEsate/import_data.csv"
simple_data_link = "http://quickstats.censusdata.abs.gov.au/census_services/getproduct/census/2016/quickstat/POA{}?opendocument"
profile_link = "http://quickstats.censusdata.abs.gov.au/census_services/getproduct/census/2016/communityprofile/POA{}?opendocument"


if __name__ == "__main__":
    import_area = pd.read_csv(source_data)
    for postcode in import_area['Postcode']:
        print(simple_data_link.format(postcode))