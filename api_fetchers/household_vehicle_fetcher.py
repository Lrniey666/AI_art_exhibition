# household_vehicle_fetcher.py

import requests
import json
from mysite.models import Vehicle  # replace app_name with your actual app name
from Data_masage.tack_out import get_city_names as City

app_id = 'c111118128-fd01fb23-e742-45ca'
app_key = '95e547e9-568e-45fc-a3c5-497c29675d5d'

auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
url ="https://tdx.transportdata.tw/api/advanced/v1/SocialEconomic/HouseholdVehicleOwnership/Year/2023/City/Taipei?%24format=JSON"



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
    try:
        d = Data(app_id, app_key, auth_response)
        data_response = requests.get(url, headers=d.get_data_header())
    except:
        a = Auth(app_id, app_key)
        auth_response = requests.post(auth_url, a.get_auth_header())
        d = Data(app_id, app_key, auth_response)
        data_response = requests.get(url, headers=d.get_data_header())    

    data_json = data_response.json()
    results = data_json.get('Results', [])

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

                # Assume you have a Vehicle model in your app with these fields
                # if not, replace this with appropriate model and fields
                Vehicle.objects.update_or_create(city_name=city_name, county_code=county_code, month=month, vehicle_type=vehicle_type, value=value)
