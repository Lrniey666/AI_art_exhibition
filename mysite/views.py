from django.shortcuts import render
from mysite.models import Vehicle
from django.http import HttpResponse
import requests, json
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random   #匯入亂數模組
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd
from api_fetchers.household_income_fetcher import fetch_and_store_income_data as fasid
from api_fetchers.UACSS_fetcher import fetch_and_store_UACSS_data as fasuad
from Data_masage.vehicle_quantity_ranking import get_new_vehicle as gnv,get_vehicle_latest_year_month as gvlyrm,vehicle_ranking as vr
<<<<<<< HEAD
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()


=======
from Data_masage.vehicle_income_growing_compare import get_Household_income as ghi ,get_income_renew_time as girt,get_all_vehicle_until_income_renew as gavuir
>>>>>>> 3919ed7a5521716800052ee28ee5836d55fc0c4e

def index(request):
    #fasvd()  # Fetch and store data
    #fasid()
    #fasuad()
    mynames = ["第十組"]
    myname = random.choice(mynames)
    #print(vr())
    #print(ghi())
    #print(gavuir())
    return render(request, "index.html", locals())

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

def vehicle_quantity_ranking(request):
    # 假設您的資料庫模型是 Vehicle，並且有一個名為 value 的欄位
    vehicles = Vehicle.objects.all()  # 從資料庫中獲取所有車輛

    # 將數據轉換為所需的格式，例如列表或字典
    values = [vehicle.value for vehicle in vehicles]  # 提取車輛的值
<<<<<<< HEAD
    sorted_cities = vehicle_ranking()  # 獲取排序後的城市列表
=======

    #print(vr())
    #print(ghi())
    #print(gavuir())

>>>>>>> 3919ed7a5521716800052ee28ee5836d55fc0c4e
    context = {
        'values': values,
        'sorted_cities': sorted_cities,  # 將排序後的城市列表添加到上下文中
    }

    return render(request, 'vehicle_quantity_ranking.html', context)

def car_quantity_ranking(request):
    #fasuad()
    #fasvd()
    #fasid()
    #print(ghi())
    #print(gavuir())
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    #print(vr())
    return render(request, 'car_quantity_ranking.html', locals())

def scooter_quantity_ranking(request):
    #fasuad()
    #fasvd()
    #fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    #print(vr())
    return render(request, 'scooter_quantity_ranking.html', locals())

def truck_quantity_ranking(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    #print(vr())
    return render(request, 'truck_quantity_ranking.html', locals())

def bus_quantity_ranking(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'bus_quantity_ranking.html', locals())

def vehicle_growing_up_all(request):
    #fasuad()
    #fasvd()
    #fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_all.html', locals())

def vehicle_growing_up_TP(request):
    #fasuad()
    #fasvd()
    #fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TP.html', locals())

def vehicle_growing_up_NP(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_NP.html', locals())

def vehicle_growing_up_TY(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TY.html', locals())

def vehicle_growing_up_TC(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TC.html', locals())

def vehicle_growing_up_TN(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TN.html', locals())

def vehicle_growing_up_KH(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_KH.html', locals())

def Income_and_vehicle_all(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_all.html', locals())

def Income_and_vehicle_car(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_car.html', locals())

def Income_and_vehicle_scooter(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_scooter.html', locals())

def student_and_vehicle_scooter(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'student_and_vehicle_scooter.html', locals())

def student_and_vehicle_car(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'student_and_vehicle_car.html', locals())
    print(vr())

