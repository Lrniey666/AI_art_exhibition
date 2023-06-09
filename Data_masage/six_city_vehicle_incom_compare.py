import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import Vehicle,Household_income
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Data_masage.tack_out import get_six_citys_Data as gscd
from Data_masage.vehicle_income_growing_compare import get_income_renew_time as girt , get_Household_income as ghi

def get_six_city_vehicle_data_as_income_renew_year():
    # Fetch the vehicle data
    latest_year = girt()
    city_names = gscd()

    vehicles = Vehicle.objects.filter(year=latest_year, month=12, city_name__in=city_names)#一律取Household_income最新年分12月
    city_values = {}
    for vehicle in vehicles:
        if vehicle.city_name in city_values:
            city_values[vehicle.city_name] += vehicle.value
        else:
            city_values[vehicle.city_name] = vehicle.value

    result = [[city, city_values.get(city, 0)] for city in city_names]
    return result

def get_six_city_car_data_as_income_renew_year():
    # Fetch the vehicle data
    latest_year = girt()
    city_names = gscd()

    vehicles = Vehicle.objects.filter(year=latest_year, month=12, vehicle_type__in=["小客車","小貨車"], city_name__in=city_names)#一律取Household_income最新年分12月
    city_values = {}
    for vehicle in vehicles:
        if vehicle.city_name in city_values:
            city_values[vehicle.city_name] += vehicle.value
        else:
            city_values[vehicle.city_name] = vehicle.value

    result = [[city, city_values.get(city, 0)] for city in city_names]
    return result

def get_six_city_scooter_data_as_income_renew_year():
    # Fetch the vehicle data
    latest_year = girt()
    city_names = gscd()

    vehicles = Vehicle.objects.filter(year=latest_year, month=12, vehicle_type="機車", city_name__in=city_names)#一律取Household_income最新年分12月
    city_values = {}
    for vehicle in vehicles:
        if vehicle.city_name in city_values:
            city_values[vehicle.city_name] += vehicle.value
        else:
            city_values[vehicle.city_name] = vehicle.value

    result = [[city, city_values.get(city, 0)] for city in city_names]
    return result

def get_new_Household_income():
    # Fetch the target year
    target_year = str(girt())
    #print(target_year)

    # Get the six city names
    six_city_names = gscd()
    #print(six_city_names)

    # Fetch all Household_income data for the target year and the six cities
    income_data = Household_income.objects.filter(year=target_year, city_name__in=six_city_names)

    # Convert to list of lists and sort
    income_data_sorted = []
    for income in income_data:
        income_data_sorted.append([income.year, income.city_name, income.Avg_number_of_househods, income.Avg_number_of_employment, income.Avg_number_of_income, income.Total])
    #print(income_data_sorted)
    # Get the city name ordering
    city_ordering = gscd()
    #print(city_ordering)
    # Sort by year, then by city name according to the order in city_ordering
    income_data_sorted.sort(key=lambda x: (x[0], city_ordering.index(x[1])))

    return income_data_sorted


