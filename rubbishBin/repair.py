import json
import uuid

import requests
from handler import repair_handler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from requests_toolbelt.multipart.encoder import MultipartEncoder
from requests_toolbelt import MultipartEncoder


def repairReport(request):
    repair_user_id = request.user_id
    file = request.FILES['file']
    # with open('/Users/lwd011204/Desktop/rubbish_service/rubbish_bin/rubbishBin/截屏2024-01-16 19.55.15.png','rb') as fp:
    #   m = MultipartEncoder(fields = {
    #     'file':('test.jpg',file.file.getvalue())
    # })
    # #   print(type(file.file.getvalue()),type(fp))
    #   res = requests.post("http://127.0.0.1:7001/uploadPhoto",m,headers={"content-type":m.content_type})
    #   print(res)
    #   fp.close()
    repair_memo = request.POST['memo']
    url = "http://121.40.59.97:7001/uploadPhoto"

    filename = str(uuid.uuid4()) + '.jpg'
    m = MultipartEncoder(fields={
        'file': (filename, file.file.getvalue())
    })

    headers = {
        "content-type": m.content_type
    }
    res = requests.post(url, m, headers=headers).json()
    if not res["success"]:
        raise Exception(res["errMsg"])
    result = repair_handler.RepairHandler.placeRepairRecordHandler(repair_user_id, repair_memo, res["url"])
    return 1


def queryRepairList(request):
    repair_userid = request.user_id
    data = repair_handler.RepairHandler.queryRepairListHandler(repair_userid)
    return data


def queryRepairDetail(request):
    params = request.body.get("data")
    repair_id = params['repair_id']
    data = repair_handler.RepairHandler.queryRepairDetail(repair_id)
    return data


def queryRepairData(request):
    data = repair_handler.RepairHandler.queryRepairDataHandler()
    return data


def changeRepairStatus(request):
    repair_id = request.body.get("repair_id", None)
    repair_status = request.body.get("repair_status",None)
    if not repair_id or not repair_status:
        return False
    data = repair_handler.RepairHandler.changeRepairStatusHandler(repair_id,repair_status)
    return data
