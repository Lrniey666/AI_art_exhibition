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


def get_all_Household_income():
    # 获取所有 Household_income 数据
    income_data = Household_income.objects.all()

    # 创建一个字典用于存储每个年度的收入总和
    income_totals = {}

    for income in income_data:
        year = income.year
        income_amount = income.Total

        # 检查字典中是否已存在该年份的收入总和，如果不存在则创建一个新的列表
        if year not in income_totals:
            income_totals[year] = 0

        # 将该城市的收入添加到对应年份的总和中
        income_totals[year] += income_amount

    # 返回每个年度的收入总和
    income_data_formatted = [income for income in income_totals.values()]

    return income_data_formatted





def get_Household_income(city_name):
    # Fetch all Household_income data for the specified city
    income_data = Household_income.objects.filter(city_name=city_name)

    # Convert to list of lists and sort
    income_data_sorted = []
    for income in income_data:
        income_data_sorted.append([income.year, income.city_name, income.Avg_number_of_househods, income.Avg_number_of_employment, income.Avg_number_of_income, income.Total])

    # Sort by year in ascending order
    income_data_sorted.sort(key=lambda x: x[0])
    # Get the most recent year
    most_recent_year = income_data_sorted[-1][0]

    # Filter data for each year until the most recent year
    filtered_data = [item[5] for item in income_data_sorted if item[0] <= most_recent_year]

    return filtered_data




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

    # Calculate total vehicles for each year in Taipei City
    all_vehicle_totals = {}
    for data in vehicle_data_sorted:
        year = data[0]
        city_name = data[1]
        vehicle_count = data[3]

        if city_name == '臺北市' or city_name == '新北市' or city_name == '桃園市'or city_name == '臺中市'or city_name == '臺南市'or city_name == '高雄市'or city_name == '新竹縣'or city_name == '苗栗縣'or city_name == '彰化縣'or city_name == '南投縣'or city_name == '雲林縣'or city_name == '嘉義縣'or city_name == '屏東縣'or city_name == '宜蘭縣'or city_name == '花蓮縣'or city_name == '臺東縣'or city_name == '澎湖縣'or city_name == '金門縣'or city_name == '連江縣'or city_name == '基隆市'or city_name == '新竹市'or city_name == '嘉義市':
            if year in all_vehicle_totals:
                all_vehicle_totals[year] += vehicle_count
            else:
                all_vehicle_totals[year] = vehicle_count

    return all_vehicle_totals


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















print(get_all_Household_income())