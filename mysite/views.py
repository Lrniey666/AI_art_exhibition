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
from Data_masage.vehicle_quantity_ranking import get_new_vehicle as gnv,get_vehicle_latest_year_month as gvlyrm, vehicle_bus_ranking, vehicle_car_ranking,vehicle_ranking as vr, vehicle_sc_ranking, vehicle_truck_ranking
from Data_masage.six_city_vehicle_incom_compare import get_six_city_car_data_as_income_renew_year as sccair,get_six_city_scooter_data_as_income_renew_year as scsair, get_new_Household_income as gnhi,\
                                                    get_six_city_vehicle_data_as_income_renew_year as scvair,get_six_city_new_population_quantity_vic as npqv,find_old_time_vic as fotv,get_six_city_population_avg_vehicle,get_six_city_month_PCI,get_six_city_population_avg_car,get_six_city_population_avg_scooter
from Data_masage.six_city_students_and_vehicle import get_students_renew_time as gsrt,get_six_city_new_students_quantity as svs,get_population_stats_time as gpst,find_old_time as fot,\
                                                    get_six_city_new_population_quantity as svp,get_fot_car_quantity as gfcq,get_fot_motorcycle_quantity as gfmq,get_fot_vehicle_quantity as gfvq,get_six_city_students_proportion,get_six_city_car_proportion,get_six_city_motorcycle_proportion
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Data_masage.vehicle_income_growing_compare import get_all_vehicle_until_income_renew,get_Household_income,get_tp_vehicle_until_income_renew,get_np_vehicle_until_income_renew,get_ty_vehicle_until_income_renew,get_tc_vehicle_until_income_renew,get_tn_vehicle_until_income_renew,get_kh_vehicle_until_income_renew,get_all_Household_income
from .models import Household_income

def index(request):
    


    mynames = ["第十組"]
    myname = random.choice(mynames)
    
    return render(request, "index.html", locals())



def vehicle_quantity_ranking(request): 
    #faspsd() 
    vehicle_data = vr()  # 調用vehicle_ranking()函數獲取數據
    time = gvlyrm()
    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量

    context = {
        'year' : time[0],
        'month' : time[1],
        'city_names': city_names,
        'values': values,
    }


    return render(request, 'vehicle_quantity_ranking.html', context)

def car_quantity_ranking(request):

    vehicle_data = vehicle_car_ranking()  # 調用vehicle_ranking()函數獲取數據
    time = gvlyrm()
    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量


    context = {
        'year' : time[0],
        'month' : time[1],
        'city_names': city_names,
        'values': values,
    }

   

    return render(request, 'car_quantity_ranking.html',context )
    

    


def scooter_quantity_ranking(request):

    vehicle_data = vehicle_sc_ranking()  # 調用vehicle_ranking()函數獲取數據
    time = gvlyrm()
    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量


    context = {
        'year' : time[0],
        'month' : time[1],
        'city_names': city_names,
        'values': values,
    }

   

    return render(request, 'scooter_quantity_ranking.html',context )
    

def truck_quantity_ranking(request):

    vehicle_data = vehicle_truck_ranking()  # 調用vehicle_ranking()函數獲取數據
    time = gvlyrm()
    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量


    context = {
        'year' : time[0],
        'month' : time[1],
        'city_names': city_names,
        'values': values,
    }

   

    return render(request, 'truck_quantity_ranking.html',context )
    
def bus_quantity_ranking(request):

    vehicle_data = vehicle_bus_ranking()  # 調用vehicle_ranking()函數獲取數據
    time = gvlyrm()
    # 將數據轉換為所需的格式
    city_names = [entry[0] for entry in vehicle_data]  # 提取城市名稱
    values = [entry[1] for entry in vehicle_data]  # 提取車輛數量


    context = {
        'year' : time[0],
        'month' : time[1],
        'city_names': city_names,
        'values': values,
    }

   

    return render(request, 'bus_quantity_ranking.html',context )

def vehicle_growing_up_all(request):

    all_vehicle_totals = get_all_vehicle_until_income_renew()
    income_data_formatted = get_all_Household_income()

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'all_vehicle_totals': all_vehicle_totals,
        'income_data_formatted': income_data_formatted,
    }
    return render(request, 'vehicle_growing_up_all.html', locals())

def vehicle_growing_up_TP(request):
    city_name = "臺北市"
    tp_vehicle_totals = get_tp_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'tp_vehicle_totals' : tp_vehicle_totals,
        'filtered_data' : filtered_data
    }
    return render(request, 'vehicle_growing_up_TP.html', locals())

def vehicle_growing_up_NP(request):
    city_name = "新北市"
    np_vehicle_totals = get_np_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'np_vehicle_totals' : np_vehicle_totals,
        'filtered_data' : filtered_data
    }
    return render(request, 'vehicle_growing_up_NP.html', locals())

def vehicle_growing_up_TY(request):
    city_name = "桃園市"
    ty_vehicle_totals = get_ty_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'ty_vehicle_totals' : ty_vehicle_totals,
        'filtered_data' : filtered_data
        }
    return render(request, 'vehicle_growing_up_TY.html', locals())

def vehicle_growing_up_TC(request):
    city_name = "臺中市"
    tc_vehicle_totals = get_tc_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'tc_vehicle_totals' : tc_vehicle_totals,
        'filtered_data' : filtered_data
    }
    return render(request, 'vehicle_growing_up_TC.html', locals())

def vehicle_growing_up_TN(request):
    city_name = "臺南市"
    tn_vehicle_totals = get_tn_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'tn_vehicle_totals' : tn_vehicle_totals,
        'filtered_data' : filtered_data
    }
    return render(request, 'vehicle_growing_up_TN.html', locals())

def vehicle_growing_up_KH(request):
    city_name = "高雄市"
    kh_vehicle_totals = get_kh_vehicle_until_income_renew()
    filtered_data = get_Household_income(city_name)
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'kh_vehicle_totals' : kh_vehicle_totals,
        'filtered_data' : filtered_data
    }
    return render(request, 'vehicle_growing_up_KH.html', locals())

def Income_and_vehicle_all(request):

    six_city_population_avg_vehicl = get_six_city_population_avg_vehicle()
    six_city_month_PCI = get_six_city_month_PCI()

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'six_city_population_avg_vehicl': six_city_population_avg_vehicl,
        'six_city_month_PCI': six_city_month_PCI,
    }
    return render(request, 'Income_and_vehicle_all.html', locals())

def Income_and_vehicle_car(request):
    six_city_population_avg_car = get_six_city_population_avg_car()
    six_city_month_PCI = get_six_city_month_PCI()

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'six_city_population_avg_car': six_city_population_avg_car,
        'six_city_month_PCI': six_city_month_PCI,
    }
    return render(request, 'Income_and_vehicle_car.html', locals())

def Income_and_vehicle_scooter(request):

    six_city_population_avg_scooter = get_six_city_population_avg_scooter()
    six_city_month_PCI = get_six_city_month_PCI()

    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'six_city_population_avg_scooter': six_city_population_avg_scooter,
        'six_city_month_PCI': six_city_month_PCI,
    }
    return render(request, 'Income_and_vehicle_scooter.html', locals())

def student_and_vehicle_scooter(request):
    six_city_students_proportion = get_six_city_students_proportion()
    six_city_motorcycle_proportion = get_six_city_motorcycle_proportion()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'six_city_students_proportion': six_city_students_proportion,
        'six_city_motorcycle_proportion' : six_city_motorcycle_proportion
    }
    return render(request, 'student_and_vehicle_scooter.html', locals())

def student_and_vehicle_car(request):
    six_city_students_proportion = get_six_city_students_proportion()
    six_city_car_proportion = get_six_city_car_proportion()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {
        'six_city_students_proportion': six_city_students_proportion,
        'six_city_car_proportion' : six_city_car_proportion
    }

    return render(request, 'student_and_vehicle_car.html', locals())
    print(vr())

