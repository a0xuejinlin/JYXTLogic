from django.shortcuts import render

from django.http import JsonResponse

import sqlite3
import pandas as pd
from datetime import datetime
import json 


# Create your views here.
def index(request):
    sql_cmd = "SELECT * FROM MinuteStock15 limit 0,10"
    cx = sqlite3.connect(r'D:\githubsharefile\JYsjadkj\mystock.db')
    result = pd.read_sql(sql=sql_cmd, con=cx)
    df_json = result.to_json(orient = 'table', force_ascii = False)
    data = json.loads(df_json)

    return JsonResponse(data, safe=False)


def spec(request):
    specname = request.GET.get('specname', 'id')
    order = request.GET.get('order', 'desc')
    isAbs = request.GET.get('abs', 'false')
    orderbyvalue = specname
    if isAbs == 'true':
        orderbyvalue = "abs(" + specname + ")"
    print(specname, order, isAbs, orderbyvalue)
    cx = sqlite3.connect(r'D:\githubsharefile\JYsjadkj\mystock.db')
    sql_cmd = "SELECT * FROM MinuteStock15 where date=(select max(date) from MinuteStock15) and " + specname + " != 'NaN' order by " + orderbyvalue + " " + order + " limit 0,50"
    
    result = pd.read_sql(sql=sql_cmd, con=cx)
    df_json = result.to_json(orient = 'table', force_ascii = False)
    data = json.loads(df_json)

    return JsonResponse(data, safe=False)

def dayk(request):
    codename = request.GET.get('code', 'sh.000652')
    order = 'desc'
    print(codename, order)
    cx = sqlite3.connect(r'D:\githubsharefile\JYsjadkj\mystock.db')
    sql_cmd = "SELECT * FROM MinuteStock15 where code='" + codename +"' order by date desc limit 0,500"
    
    result = pd.read_sql(sql=sql_cmd, con=cx)

    df_json = result.to_json(orient = 'table', force_ascii = False)
    data = json.loads(df_json)

    return JsonResponse(data, safe=False)