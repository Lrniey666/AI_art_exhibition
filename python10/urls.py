from django.contrib import admin
from django.urls import path
from mysite import views   # 引入views.py中所有的函式

urlpatterns = [
    path('', views.index, name='index'),      # add a name to the URL pattern
    path('admin/', admin.site.urls),
    path('vehicle_quantity_ranking/', views.vehicle_quantity_ranking),
    path('car_quantity_ranking/', views.car_quantity_ranking),
    path('scooter_quantity_ranking/', views.scooter_quantity_ranking),
    path('truck_quantity_ranking/', views.truck_quantity_ranking),
    path('bus_quantity_ranking/', views.bus_quantity_ranking),
]
