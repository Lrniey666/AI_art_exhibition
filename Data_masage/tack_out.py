from mysite.models import City_name

def get_city_names():
    city_names = City_name.objects.values_list('city_English_name', 'city_Chinese_name')
    return list(city_names)
