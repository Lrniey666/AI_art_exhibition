from django.contrib import admin
from mysite.models import Tdx_api,Vehicle,City_name,Household_income,Universities_and_colleges_Student_status,Data_renew_time,Population_stats

# Register your models here.
admin.site.register(Tdx_api)
admin.site.register(Vehicle)
admin.site.register(City_name)
admin.site.register(Household_income)
admin.site.register(Universities_and_colleges_Student_status)
admin.site.register(Data_renew_time)
admin.site.register(Population_stats)