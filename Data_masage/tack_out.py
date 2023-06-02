import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()
from mysite.models import City_name,Tdx_api
api_turn=0

def get_city_names():
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    city_names = City_name.objects.values_list('city_English_name', 'city_Chinese_name')
    return list(city_names)

def get_TDX_API():
    global api_turn
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    api = Tdx_api.objects.values_list('api_id', 'api_key')
    aapi=(list(api))[api_turn]
    print(api_turn)
    if api_turn <  len(api)-1:
       api_turn+=1
    else:
       api_turn=0     
    return aapi
