import sys
import os
sys.path.append('C:\\python-10')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
import django
django.setup()

from mysite.models import City_name

def get_city_names():
    sys.path.append('C:\\python-10')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'python10.settings'
    city_names = City_name.objects.values_list('city_English_name', 'city_Chinese_name')
    return list(city_names)

if __name__ == '__main__':
    cn=get_city_names()
    print(cn)
