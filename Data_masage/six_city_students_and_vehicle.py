#six_city_students_and_vehicle.py
import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import Vehicle,Universities_and_colleges_Student_status as uacss,Population_stats as ps
from Data_masage.tack_out import get_six_citys_Data as gscd
from datetime import datetime

def get_students_renew_time():
    # Fetch all Universities_and_colleges_Student_status data
    student_data = uacss.objects.all()
    # Find the max year
    max_year = max(student.year for student in student_data)
    return int(max_year)

def get_population_stats_time():
    # Fetch all population data
    population_data = ps.objects.all()

    # Find the max year
    max_year = max(population.Year for population in population_data)

    # Find the population data of the max year
    population_data_max_year = ps.objects.filter(Year=max_year)

    # Find the max month in the max year
    max_month = max(population.Month for population in population_data_max_year)

    return [int(max_year), int(max_month)]


def find_old_time():#比誰最新資料年份較舊
    a=get_students_renew_time()
    b=(get_population_stats_time())[0]
    if a<b:
        return a
    else:
        return b

def get_six_city_new_students_quantity():
    # Fetch the target year
    target_year = str(find_old_time())

    # Get the six city names
    six_city_names = gscd()

    # Fetch all student data for the target year and the six cities
    student_data = uacss.objects.filter(year=target_year, city_name__in=six_city_names)

    # Initialize the city data
    city_data = {city: [0, 0, 0] for city in six_city_names}

    # Sum up the number of males, females, and total for each city
    for student in student_data:
        city_data[student.city_name][0] += int(student.NumberOfMales)
        city_data[student.city_name][1] += int(student.NumberOfFemales)
        city_data[student.city_name][2] += int(student.Total)

    # Convert to list of lists
    city_data_list = [[city, *data] for city, data in city_data.items()]

    return city_data_list

def get_six_city_new_population_quantity():
    # Fetch the target year
    target_year = str(find_old_time())

    # Get the six city names
    six_city_names = gscd()

    # Fetch all population data for the target year and the six cities in December
    population_data = ps.objects.filter(Year=target_year, CityName__in=six_city_names, Month=str((get_population_stats_time())[1]))

    # Initialize the city data
    city_data = {city: [0, 0, 0] for city in six_city_names}

    # Sum up the number of males, females, and total population for each city
    for population in population_data:
        city_data[population.CityName][0] += population.NumberOfMales
        city_data[population.CityName][1] += population.NumberOfFemales
        city_data[population.CityName][2] += population.NumberOfPopulation

    # Convert to list of lists
    city_data_list = [[city, *data] for city, data in city_data.items()]

    return city_data_list

def get_fot_vehicle_quantity():
    # Fetch the target year and month
    target_year = find_old_time()
    target_month = get_population_stats_time()[1]

    # Get the six city names
    six_city_names = gscd()

    # Fetch all vehicle data for the target year, month and the six cities
    vehicle_data = Vehicle.objects.filter(year=target_year, month=target_month, city_name__in=six_city_names)

    # Initialize the city data
    city_data = {city: 0 for city in six_city_names}

    # Sum up the value for each city
    for vehicle in vehicle_data:
        city_data[vehicle.city_name] += int(vehicle.value)

    # Convert to list of lists
    city_data_list = [[city, data] for city, data in city_data.items()]

    return city_data_list

def get_fot_car_quantity():
    # Fetch the target year and month
    target_year = find_old_time()
    target_month = get_population_stats_time()[1]

    # Get the six city names
    six_city_names = gscd()

    # Fetch all vehicle data for the target year, month, the six cities, and vehicle type is car
    vehicle_data = Vehicle.objects.filter(year=target_year, month=target_month, city_name__in=six_city_names, vehicle_type='小客車')

    # Initialize the city data
    city_data = {city: 0 for city in six_city_names}

    # Sum up the value for each city
    for vehicle in vehicle_data:
        city_data[vehicle.city_name] += int(vehicle.value)

    # Convert to list of lists
    city_data_list = [[city, data] for city, data in city_data.items()]

    return city_data_list

def get_fot_motorcycle_quantity():
    # Fetch the target year and month
    target_year = find_old_time()
    target_month = get_population_stats_time()[1]

    # Get the six city names
    six_city_names = gscd()

    # Fetch all vehicle data for the target year, month, the six cities, and vehicle type is motorcycle
    vehicle_data = Vehicle.objects.filter(year=target_year, month=target_month, city_name__in=six_city_names, vehicle_type='機車')

    # Initialize the city data
    city_data = {city: 0 for city in six_city_names}

    # Sum up the value for each city
    for vehicle in vehicle_data:
        city_data[vehicle.city_name] += int(vehicle.value)

    # Convert to list of lists
    city_data_list = [[city, data] for city, data in city_data.items()]

    return city_data_list

"""
以下為前台較會用到的函式
"""

def get_six_city_students_proportion():
    """
    功能: 
    計算六大城市中每個城市學生人數佔總人口的比例。
    此函式使用 get_six_city_new_students_quantity() 和 get_six_city_new_population_quantity() 的結果，
    產生一個列表，其中每個內部列表由城市名稱和該城市的學生比例組成。

    輸出格式:
    [['城市名稱(str)', 學生比例(float)],...]
    """

    # Get the student quantity and population quantity for each city
    students_quantity = get_six_city_new_students_quantity()
    population_quantity = get_six_city_new_population_quantity()

    # Convert the lists of lists into dictionaries for easier data manipulation
    students_quantity_dict = {item[0]: item[3] for item in students_quantity}
    population_quantity_dict = {item[0]: item[3] for item in population_quantity}

    # Initialize the city data
    city_data = {}

    # Calculate the proportion of students to the total population for each city
    for city, students in students_quantity_dict.items():
        city_data[city] = round(students / population_quantity_dict[city], 4)


    # Convert the dictionary to a list of lists
    city_data_list = [[city, proportion] for city, proportion in city_data.items()]

    return city_data_list

def get_six_city_car_proportion():
    """
    功能: 
    計算六大城市中，每個城市的汽車數量佔總車輛數量的比例。
    此函數使用 get_fot_car_quantity() 和 get_fot_vehicle_quantity() 的結果，
    生成一個列表，其中每個內部列表由城市名稱和該城市的汽車比例組成。

    輸出格式:
    [['城市名稱', 汽車比例(float)],...]
    """
    # 獲取每個城市的汽車數量和總車輛數量
    car_quantity = get_fot_car_quantity()
    vehicle_quantity = get_fot_vehicle_quantity()

    # 將列表轉換為字典，以便於數據操作
    car_quantity_dict = {item[0]: item[1] for item in car_quantity}
    vehicle_quantity_dict = {item[0]: item[1] for item in vehicle_quantity}

    # 初始化城市數據
    city_data = {}

    # 為每個城市計算汽車數量佔總車輛數量的比例
    for city, cars in car_quantity_dict.items():
        city_data[city] = round(cars / vehicle_quantity_dict[city], 4)


    # 將字典轉換為列表
    city_data_list = [[city, proportion] for city, proportion in city_data.items()]

    return city_data_list


def get_six_city_motorcycle_proportion():
    """
    功能: 
    計算六大城市中，每個城市的機車數量佔總車輛數量的比例。
    此函數使用 get_fot_motorcycle_quantity() 和 get_fot_vehicle_quantity() 的結果，
    生成一個列表，其中每個內部列表由城市名稱和該城市的機車比例組成。

    輸出格式:
    [['城市名稱', 機車比例(float)],...]
    """
    # 獲取每個城市的機車數量和總車輛數量
    motorcycle_quantity = get_fot_motorcycle_quantity()
    vehicle_quantity = get_fot_vehicle_quantity()

    # 將列表轉換為字典，以便於數據操作
    motorcycle_quantity_dict = {item[0]: item[1] for item in motorcycle_quantity}
    vehicle_quantity_dict = {item[0]: item[1] for item in vehicle_quantity}

    # 初始化城市數據
    city_data = {}

    # 為每個城市計算機車數量佔總車輛數量的比例
    for city, motorcycles in motorcycle_quantity_dict.items():
        city_data[city] = round(motorcycles / vehicle_quantity_dict[city], 4)


    # 將字典轉換為列表
    city_data_list = [[city, proportion] for city, proportion in city_data.items()]

    return city_data_list




if __name__ == "__main__":

    print(get_students_renew_time())
    print(get_population_stats_time())
    print(find_old_time())
    print(get_six_city_new_students_quantity())
    print(get_six_city_new_population_quantity())
    print(get_fot_vehicle_quantity())
    print(get_fot_car_quantity())
    print(get_fot_motorcycle_quantity())
    print(get_six_city_students_proportion())
    print(get_six_city_car_proportion())
    print(get_six_city_motorcycle_proportion())