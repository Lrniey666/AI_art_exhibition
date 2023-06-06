import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import City_name,Tdx_api,Vehicle
from datetime import datetime
from dateutil.relativedelta import relativedelta
api_turn=0

def get_city_names():
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    city_names = City_name.objects.values_list('city_English_name', 'city_Chinese_name')
    return list(city_names)

def get_TDX_API():
    global api_turn
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    api = Tdx_api.objects.values_list('api_id', 'api_key')
    aapi=(list(api))[api_turn]
    print(api_turn)
    if api_turn <  len(api)-1:
       api_turn+=1
    else:
       api_turn=0     
    return aapi

def get_six_citys_Data():
    six_citys=["臺北市","新北市","桃園市","臺中市","臺南市","高雄市"]
    return six_citys

def get_vehicle_latest_year_month():
    # Start from the current year and month
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    
    vehicles = Vehicle.objects.filter(year=year, month=month)

    # If there's no data for the current year and month, keep going back one month at a time
    while not vehicles.exists():
        current_date -= relativedelta(months=1)
        year = current_date.year
        month = current_date.month
        vehicles = Vehicle.objects.filter(year=year, month=month)

    return [year, month]

def get_new_vehicle():
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    django.setup()

    # Get the latest year and month
    year_month = get_vehicle_latest_year_month()
    year = year_month[0]
    month = year_month[1]

    # Get the vehicles for that year and month
    vehicles = Vehicle.objects.filter(year=year, month=month)

    # Build the list
    result = []
    for vehicle in vehicles:
        result.append([vehicle.city_name, vehicle.vehicle_type, vehicle.value])

    return result

def summarize_and_sort_vehicle_data():
    # Fetch the vehicle data
    vehicle_data = get_new_vehicle()

    # Initialize a dictionary to hold the total value for each city
    city_totals = {}

    # For each entry in the vehicle data...
    for entry in vehicle_data:
        city_name = entry[0]
        value = entry[2]

        # If this city is not yet in the dictionary, add it with a total value of 0
        if city_name not in city_totals:
            city_totals[city_name] = 0

        # Add the value for this entry to the city's total
        city_totals[city_name] += value

    # Now we want to sort the cities by total value. We'll use a list of tuples for this.
    # Each tuple will be (city_name, total_value), and we'll sort them by total_value.
    sorted_cities = sorted(city_totals.items(), key=lambda item: item[1], reverse=True)

    return sorted_cities


