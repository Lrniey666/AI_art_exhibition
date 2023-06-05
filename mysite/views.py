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
from datetime import datetime
from dateutil.relativedelta import relativedelta


def index(request):
    #fasvd()  # Fetch and store data
    #fasid()
    #fasuad()
    mynames = ["第十組"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())
    print(vr())


def vehicle_quantity_ranking(request):
    vehicle_data = vr()  # 調用vehicle_ranking()函數獲取數據

    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量

    context = {
        'city_names': city_names,
        'values': values,
    }

    return render(request, 'vehicle_quantity_ranking.html', context)

def car_quantity_ranking(request):
    #fasuad()
    #fasvd()
    #fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'car_quantity_ranking.html', locals())
    print(vr())

def scooter_quantity_ranking(request):
    #fasuad()
    #fasvd()
    #fasid()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'scooter_quantity_ranking.html', locals())
    print(vr())

def truck_quantity_ranking(request):
    #fasuad()
    #fasid()
    #fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'truck_quantity_ranking.html', locals())
    print(vr())
    
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

