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

def get_income_renew_time():
    # Fetch all Household_income data
    income_data = Household_income.objects.all()

    # Find the max year
    max_year = max(income.year for income in income_data)

    return int(max_year)


def get_Household_income():
    # Fetch all Household_income data
    income_data = Household_income.objects.all()

    # Convert to list of lists and sort
    income_data_sorted = []
    for income in income_data:
        income_data_sorted.append([income.year, income.city_name, income.Avg_number_of_househods, income.Avg_number_of_employment, income.Avg_number_of_income, income.Total])

    # Get the city name ordering
    city_ordering = [city_info[1] for city_info in gcn()]

    # Sort by year, then by city name according to the order in city_ordering
    income_data_sorted.sort(key=lambda x: (x[0], city_ordering.index(x[1])))

    return income_data_sorted

def get_all_vehicle_until_income_renew():
    # Get the latest year from Household_income data
    max_year = get_income_renew_time()

    # Fetch all Vehicle data from 2016 to max_year (December)
    vehicle_data = Vehicle.objects.filter(year__range=(2016, max_year), month=12)

    # Convert to list of lists and sort
    vehicle_data_sorted = []
    for vehicle in vehicle_data:
        vehicle_data_sorted.append([vehicle.year, vehicle.city_name, vehicle.vehicle_type, vehicle.value])

    # Get the city name ordering
    city_ordering = [city_info[1] for city_info in gcn()]

    # Sort by year, then by city name according to the order in city_ordering
    vehicle_data_sorted.sort(key=lambda x: (x[0], city_ordering.index(x[1])))

    return vehicle_data_sorted









