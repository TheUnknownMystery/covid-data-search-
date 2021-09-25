import requests
import pandas as pd
import os

#from access import URL, API_KEY

# Hey there! you can get the url from rapid api
# getting the covid data from an api

#use your own api_key!

def get_covid_data(url, api_key):

    URL = url + api_key

    covid_data = requests.get(URL)
    covid_json_data = covid_data.json()

    return pd.json_normalize(covid_json_data)


# getting the search results from the user
def covid_data_search(URL, API_KEY, req_country):
    data_frame = get_covid_data(URL, API_KEY)
    data_frame['country_code_sp'] = data_frame['Country'].str.lower()

    return data_frame[data_frame['country_code_sp'] == req_country]


def main():
    covid_searched_data_frame = covid_data_search(
        "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/USA/?rapidapi-key=", "576c3763camsha057e0f4a997877p12b661jsna39c278491d2", "united states")
    covid_searched_data_frame.head(10)


# running all the functions and displaying data
main()
