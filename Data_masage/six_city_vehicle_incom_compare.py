import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import Vehicle,Household_income
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Data_masage.tack_out import get_city_names as gcn
from Data_masage.vehicle_quantity_ranking import get_new_vehicle as gnv

six_city=["台北市","新北市","桃園市","台中市","台南市","高雄市"]

def get_vehicle_latest_year_month():
    # Start from the current year and month
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    
    vehicles = Vehicle.objects.filter(year=year, month=month)

def get_six_city_new_car_data():
    # Fetch the vehicle data
    vehicle_data = gnv()

    result = []
    # Filter by vehicle type and city
    for entry in vehicle_data:
        city_name = entry[0]
        vehicle_type = entry[1]
        value = entry[2]

        if city_name in six_city and vehicle_type in ["小客車","小貨車"]:
            result.append([city_name, value])

    return result


def get_six_city_new_scooter_data():
    # Fetch the vehicle data
    vehicle_data = gnv()

    result = []
    # Filter by vehicle type and city
    for entry in vehicle_data:
        city_name = entry[0]
        vehicle_type = entry[1]
        value = entry[2]

        if city_name in six_city and vehicle_type == "機車":
            result.append([city_name, value])       

    return result




   

   