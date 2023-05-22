from django.contrib import admin
from django.urls import path
from mysite import views   # 引入views.py中所有的函式

urlpatterns = [
    path('', views.index),      # 設定執行首頁顯示的功能由index函式負責
    path('admin/', admin.site.urls),
]