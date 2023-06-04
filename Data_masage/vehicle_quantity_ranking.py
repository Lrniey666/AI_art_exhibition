import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import Vehicle
from datetime import datetime
from dateutil.relativedelta import relativedelta


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

def vehicle_ranking():
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