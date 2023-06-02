# household_vehicle_fetcher.py

import requests
import json
from mysite.models import Vehicle  # replace app_name with your actual app name
from Data_masage.tack_out import get_city_names as City , get_TDX_API as GTA
from datetime import datetime

app_id = 'c111118128-e3258c81-c7da-4126'
app_key = '130c417a-36e8-45f9-ace8-f177ac6b1a52'

auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
url ="https://tdx.transportdata.tw/api/advanced/v1/SocialEconomic/HouseholdVehicleOwnership/Year/2023/City/Taipei?%24format=JSON"

now_time = datetime.now()
year = now_time.year
month =now_time.month
day = now_time.day
date_list = [year, month, day]


class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        content_type = 'application/x-www-form-urlencoded'
        grant_type = 'client_credentials'

        return{
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

def fetch_and_store_vehicle_data():
    city_names = City()  # get city names
    current_year = date_list[0]  # get current year from date_list

    for year in range(current_year-1, current_year+1):  # iterate from 2016 to current year
        for city in city_names:  # iterate over all cities
            city_name_en = city[0]  # get English name of city
            print(year)
            print(city[0])

            # construct the url
            url = f"https://tdx.transportdata.tw/api/advanced/v1/SocialEconomic/HouseholdVehicleOwnership/Year/{year}/City/{city_name_en}?%24format=JSON"

            try:
                api_list=GTA()
                app_id=api_list[0]
                app_key=api_list[1]
                print(app_id)
                print(app_key)
                a = Auth(app_id, app_key)
                auth_response = requests.post(auth_url, a.get_auth_header())
                d = Data(app_id, app_key, auth_response)
                data_response = requests.get(url, headers=d.get_data_header())
                data_json = data_response.json()
                results = data_json.get('Results', [])
                
                if not results:  # if results is empty, skip the current iteration
                    print(f"No data for {city_name_en} in {year}")
                    continue

                for result in results:
                    city_name = result.get('CityName')
                    county_code = result.get('CountyCode')
                    vehicle_data = result.get('VehicleData', [])
                    
                    for month_data in vehicle_data:
                        month = month_data.get('Month')
                        vehicles = month_data.get('Vehicles', [])

                        for vehicle in vehicles:
                            vehicle_type = vehicle.get('Type')
                            value = vehicle.get('Value')
                            
                            Vehicle.objects.update_or_create(year=year,city_name=city_name, county_code=county_code, month=month, vehicle_type=vehicle_type, value=value)
            
            except Exception as e:
                print(f"An error occurred: {e}")
