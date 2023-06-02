from django.shortcuts import render
from mysite.models import Vehicle
from django.http import HttpResponse
import requests, json
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random   #匯入亂數模組
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd
from api_fetchers.household_income_fetcher import fetch_and_store_income_data as fasid

def index(request):
    #fasvd()  # Fetch and store data
    fasid()
    mynames = ["第十組"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())

def vehicle_quantity_ranking(request):
    # 假設您的資料庫模型是 Vehicle，並且有一個名為 value 的欄位
    vehicles = Vehicle.objects.all()  # 從資料庫中獲取所有車輛

    # 將數據轉換為所需的格式，例如列表或字典
    values = [vehicle.value for vehicle in vehicles]  # 提取車輛的值

    context = {
        'values': values,
    }

    return render(request, 'vehicle_quantity_ranking.html', context)

def car_quantity_ranking(request):
    #fasvd()
    fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'car_quantity_ranking.html', locals())

def scooter_quantity_ranking(request):
    #fasvd()
    fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'scooter_quantity_ranking.html', locals())

def truck_quantity_ranking(request):
    fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'truck_quantity_ranking.html', locals())

def bus_quantity_ranking(request):
    fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'bus_quantity_ranking.html', locals())