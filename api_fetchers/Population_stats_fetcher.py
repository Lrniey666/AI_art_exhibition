# Population_stats_fetcher.py

import requests
import json
from mysite.models import Population_stats  # replace app_name with your actual app name
from Data_masage.tack_out import get_city_names as City, get_TDX_API as GTA
from datetime import datetime

app_id = ""
app_key = ""

auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
url =""  # this will be updated later

now_time = datetime.now()
year = now_time.year
month =now_time.month
day = now_time.day
date_list = [year, month, day]
count=0

class Auth():
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        content_type = 'application/x-www-form-urlencoded'
        grant_type = 'client_credentials'

        return {
            'content-type' : content_type,
            'grant_type' : grant_type,
            'client_id' : self.app_id,
            'client_secret' : self.app_key
        }

class Data():

    def __init__(self, app_id, app_key, auth_response):
        self.app_id = app_id
        self.app_key = app_key
        self.auth_response = auth_response

    def get_data_header(self):
        auth_JSON = json.loads(self.auth_response.text)
        access_token = auth_JSON.get('access_token')

        return{
            'authorization': 'Bearer '+access_token
        }

def fetch_and_store_Population_stats_data():
    city_names = City()  # get city names
    current_year = date_list[0]  # get current year from date_list
    no=""

    for year in range(current_year-1,current_year):  # iterate from last year to current year
        for city in city_names:  # iterate over all cities
            city_name_en = city[0]  # get English name of city

            # construct the url
            url = f"https://tdx.transportdata.tw/api/advanced/v1/SocialEconomic/PopulationStats/Year/{year}/City/{city_name_en}/Town?%24format=JSON"

            try:
                api_list=GTA()
                app_id=api_list[0]
                app_key=api_list[1]
                a = Auth(app_id, app_key)
                auth_response = requests.post(auth_url, a.get_auth_header())
                d = Data(app_id, app_key, auth_response)
                data_response = requests.get(url, headers=d.get_data_header())
                data_json = data_response.json()
                results = data_json.get('Results', [])
                
                if not results:  # if results is empty, skip the current iteration
                    print(f"No data for {city_name_en} in {year}")
                    no+=f"{city_name_en},"
                    continue
                
                for result in results:
                    city_name = result.get('CityName')
                    county_code = result.get('CountyCode')
                    town_data = result.get('TownData', [])
                    print(city_name)

                    for month_data in town_data:
                        month = month_data.get('Month')
                        towns = month_data.get('Towns', [])
                        print(month)

                        for town in towns:
                            town_name = town.get('TownName')
                            town_code = town.get('TownCode')
                            number_of_househods = town.get('NumberOfHousehods')
                            number_of_population = town.get('NumberOfPopulation')
                            number_of_males = town.get('NumberOfMales')
                            number_of_females = town.get('NumberOfFemales')
                           

                            Population_stats.objects.update_or_create(
                                Year=year,
                                CityName=city_name,
                                CountyCode=county_code,
                                Month=month,
                                TownName=town_name,
                                TownCode=town_code,
                                NumberOfHousehods=number_of_househods,
                                NumberOfPopulation=number_of_population,
                                NumberOfMales=number_of_males,
                                NumberOfFemales=number_of_females
                            )

            except Exception as e:
                print(f"Error fetching data for {city_name_en} in {year}: {e}")


