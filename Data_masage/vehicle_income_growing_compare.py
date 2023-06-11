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
    vehicle_data = Vehicle.objects.filter(year=max_year, month=12)
    

    # Calculate total vehicles by city
    total_vehicles_by_city = {}
    for vehicle in vehicle_data:
        city_name = vehicle.city_name
        vehicle_count = vehicle.value

        if city_name not in total_vehicles_by_city:
            total_vehicles_by_city[city_name] = 0

        total_vehicles_by_city[city_name] += vehicle_count

    return total_vehicles_by_city

def get_tp_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    tp_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '臺北市':
            if year in tp_vehicle_totals:
                tp_vehicle_totals[year] += vehicle_count
            else:
                tp_vehicle_totals[year] = vehicle_count

    return tp_vehicle_totals

def get_np_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    np_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '新北市':
            if year in np_vehicle_totals:
                np_vehicle_totals[year] += vehicle_count
            else:
                np_vehicle_totals[year] = vehicle_count

    return np_vehicle_totals

def get_ty_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    ty_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '桃園市':
            if year in ty_vehicle_totals:
                ty_vehicle_totals[year] += vehicle_count
            else:
                ty_vehicle_totals[year] = vehicle_count

    return ty_vehicle_totals

def get_tc_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    tc_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '臺中市':
            if year in tc_vehicle_totals:
                tc_vehicle_totals[year] += vehicle_count
            else:
                tc_vehicle_totals[year] = vehicle_count

    return tc_vehicle_totals

def get_tn_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    tn_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '臺南市':
            if year in tn_vehicle_totals:
                tn_vehicle_totals[year] += vehicle_count
            else:
                tn_vehicle_totals[year] = vehicle_count

    return tn_vehicle_totals

def get_kh_vehicle_until_income_renew():
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

    # Calculate total vehicles for each year in Taipei City
    kh_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '高雄市':
            if year in kh_vehicle_totals:
                kh_vehicle_totals[year] += vehicle_count
            else:
                kh_vehicle_totals[year] = vehicle_count

    return kh_vehicle_totals







