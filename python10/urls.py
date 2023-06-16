from django.contrib import admin
from django.urls import path
from mysite import views   # 引入views.py中所有的函式


urlpatterns = [
    path('', views.index, name='index'),      # add a name to the URL pattern
    path('admin/', admin.site.urls),
    path('vehicle_quantity_ranking/', views.vehicle_quantity_ranking, name='vehicle_quantity_ranking'),
    path('car_quantity_ranking/', views.car_quantity_ranking),
    path('scooter_quantity_ranking/', views.scooter_quantity_ranking),
    path('truck_quantity_ranking/', views.truck_quantity_ranking),
    path('bus_quantity_ranking/', views.bus_quantity_ranking),
    path('vehicle_growing_up_all/', views.vehicle_growing_up_all, name='vehicle_growing_up_all'),
    path('vehicle_growing_up_KH/', views.vehicle_growing_up_KH),
    path('vehicle_growing_up_NP/', views.vehicle_growing_up_NP),
    path('vehicle_growing_up_TC/', views.vehicle_growing_up_TC),
    path('vehicle_growing_up_TN/', views.vehicle_growing_up_TN),
    path('vehicle_growing_up_TP/', views.vehicle_growing_up_TP),
    path('vehicle_growing_up_TY/', views.vehicle_growing_up_TY),
    path('Income_and_vehicle_all/', views.Income_and_vehicle_all, name='Income_and_vehicle_all'),
    path('Income_and_vehicle_car/', views.Income_and_vehicle_car),
    path('Income_and_vehicle_scooter/', views.Income_and_vehicle_scooter),
    path('student_and_vehicle_scooter/', views.student_and_vehicle_scooter),
    path('student_and_vehicle_car/', views.student_and_vehicle_car, name='student_and_vehicle_car'),
]
