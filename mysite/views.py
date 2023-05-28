from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random   #匯入亂數模組
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd

def index(request):
    fasvd()  # Fetch and store data
    mynames = ["第十組"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())

def vehicle_quantity_ranking(request):
    fasvd()
    # 你可能需要在這裡提供給模板一些上下文資料
    context = {}
    return render(request, 'vehicle_quantity_ranking.html', locals())