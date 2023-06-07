from django.shortcuts import render
from mysite.models import Vehicle
from django.http import HttpResponse
import requests, json
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random   #匯入亂數模組
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd
from api_fetchers.household_income_fetcher import fetch_and_store_income_data as fasid
from api_fetchers.UACSS_fetcher import fetch_and_store_UACSS_data as fasuad
from api_fetchers.Population_stats_fetcher import fetch_and_store_Population_stats_data as faspsd
from Data_masage.vehicle_quantity_ranking import get_new_vehicle as gnv,get_vehicle_latest_year_month as gvlyrm,vehicle_ranking as vr
from Data_masage.six_city_vehicle_incom_compare import get_six_city_car_data_as_income_renew_year as sccair,get_six_city_scooter_data_as_income_renew_year as scsair,get_new_Household_income as gnhi
from Data_masage.six_city_students_and_vehicle import get_students_renew_time as gsrt,get_six_city_new_students_quantity as svs,get_population_stats_time as gpst,find_old_time as fot,\
                                                    get_six_city_new_population_quantity as svp,get_fot_car_quantity as gfcq,get_fot_motorcycle_quantity as gfmq,get_fot_vehicle_quantity as gfvq
from datetime import datetime
from dateutil.relativedelta import relativedelta


def index(request):


    mynames = ["第十組"]
    myname = random.choice(mynames)
    
    return render(request, "index.html", locals())



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

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
   

    return render(request, 'car_quantity_ranking.html', locals())
    

    


def scooter_quantity_ranking(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'scooter_quantity_ranking.html', locals())
    

def truck_quantity_ranking(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'truck_quantity_ranking.html', locals())
    print(vr())
    
def bus_quantity_ranking(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'bus_quantity_ranking.html', locals())

def vehicle_growing_up_all(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_all.html', locals())

def vehicle_growing_up_TP(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TP.html', locals())

def vehicle_growing_up_NP(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_NP.html', locals())

def vehicle_growing_up_TY(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TY.html', locals())

def vehicle_growing_up_TC(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TC.html', locals())

def vehicle_growing_up_TN(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_TN.html', locals())

def vehicle_growing_up_KH(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_growing_up_KH.html', locals())

def Income_and_vehicle_all(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_all.html', locals())

def Income_and_vehicle_car(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_car.html', locals())

def Income_and_vehicle_scooter(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'Income_and_vehicle_scooter.html', locals())

def student_and_vehicle_scooter(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'student_and_vehicle_scooter.html', locals())

def student_and_vehicle_car(request):

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'student_and_vehicle_car.html', locals())
    print(vr())

