from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別

def index(request):
    myname = ["第十組"]
    return render(request, "index.html", locals())