from django.contrib import admin
from mysite.models import Tdx_api,Vehicle,City_name,Household_income

# Register your models here.
admin.site.register(Tdx_api)
admin.site.register(Vehicle)
admin.site.register(City_name)
admin.site.register(Household_income)
