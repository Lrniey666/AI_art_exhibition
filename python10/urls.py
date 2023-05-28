from django.contrib import admin
from django.urls import path
from mysite import views   # 引入views.py中所有的函式

urlpatterns = [
    path('', views.index, name='index'),      # add a name to the URL pattern
    path('admin/', admin.site.urls),
    path('vehicle_quantity_ranking/', views.vehicle_quantity_ranking),
]
