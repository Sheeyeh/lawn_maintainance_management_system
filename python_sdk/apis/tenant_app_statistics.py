#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



def QueryTenantApiMonthlyCount(appKey, appSecret):
    path = '/tenant_app_statistics/queryTenantApiMonthlyCount'
    head = {}
    param = {}
    version = '20201225122609'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

def QueryTenantAppCount(appKey, appSecret):
    path = '/tenant_app_statistics/queryTenantAppCount'
    head = {}
    param = {}
    version = '20201225122611'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数dateType: 类型String, 参数不可以为空
#  描述:日期格式 m：月  d：日
#参数dataType: 类型String, 参数不可以为空
#  描述:数据格式 1：api调用量分析
def QueryTenantApiTrend(appKey, appSecret, dateType, dataType):
    path = '/tenant_app_statistics/queryTenantApiTrend'
    head = {}
    param = {'dateType':dateType, 'dataType':dataType}
    version = '20201225122606'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

