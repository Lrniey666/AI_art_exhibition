import requests
import json
from mysite.models import Household_income  # replace app_name with your actual app name
from Data_masage.tack_out import get_city_names as City , get_TDX_API as GTA
from datetime import datetime

app_id = ""
app_key = ""

auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
url =""

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
        print(auth_JSON)
        access_token = auth_JSON.get('access_token')

        return{
            'authorization': 'Bearer '+access_token
        }

def fetch_and_store_income_data():
    city_names = City()  # get city names
    current_year = date_list[0]  # get current year from date_list
    count=0
    no=""


    for year in range(current_year-1,current_year):  # iterate from last year to current year
        for city in city_names:  # iterate over all cities
            city_name_en = city[0]  # get English name of city
            print("\nincome\n")
            print(year)
            print(city[0])

            # construct the url
            url = f"https://tdx.transportdata.tw/api/advanced/v1/SocialEconomic/HouseholdIncome/Year/{year}/City/{city_name_en}?%24format=JSON"

            try:
                api_list=GTA()
                app_id=api_list[0]
                app_key=api_list[1]
                print(app_id)
                print(app_key)
                a = Auth(app_id, app_key)
                auth_response = requests.post(auth_url, a.get_auth_header())
                print(auth_response.status_code)  # Add this line to debug
                print(auth_response.text)  # Add this line to debug
                d = Data(app_id, app_key, auth_response)
                data_response = requests.get(url, headers=d.get_data_header())
                data_json = data_response.json()
                results = data_json.get('Results', [])
                
                       
                if not results:  # if results is empty, skip the current iteration
                    print(f"No data for {city_name_en} in {year}")
                    no+=f"{city_name_en},"
                    continue
                    


                for result in results:
                    print(result)
                    city_name = result.get('CityName')
                    county_code = result.get('CountyCode')
                    household_data = result.get('Household', {})

                    avg_households = household_data.get('AvgNumberOfHousehods')
                    avg_employment = household_data.get('AvgNumberOfEmployment')
                    avg_income = household_data.get('AvgNumberOfIncome')
                    total = household_data.get('Total')  # Get the Total value

                    Household_income.objects.update_or_create(
                        year=year,
                        city_name=city_name, 
                        county_code=county_code, 
                        Avg_number_of_househods=avg_households,  
                        Avg_number_of_employment=avg_employment,  
                        Avg_number_of_income=avg_income,  
                        Total=total
                    )
                    count+=1
                    print("輸入",count,"次")        
            
            except Exception as e:
                print(f"An error occurred: {e}")
    print("\n沒有",no,"\n")


if __name__ == "__main__":
    fetch_and_store_income_data()

    