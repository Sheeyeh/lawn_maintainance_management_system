#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasCreateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/createRule'
    head = {}
    param = {}
    version = '20200111000503'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数可以为空
#  描述:
#参数productId: 类型String, 参数不可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def saasQueryRule(appKey, appSecret, ruleId, productId, pageNow, pageSize):
    path = '/aep_rule_engine/api/v2/rule/sass/queryRule'
    head = {}
    param = {'ruleId':ruleId, 'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200111000633'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasUpdateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/updateRule'
    head = {}
    param = {}
    version = '20200111000540'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasDeleteRuleEngine(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/deleteRule'
    head = {}
    param = {}
    version = '20200111000611'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/createRule'
    head = {}
    param = {}
    version = '20210327062633'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/updateRule'
    head = {}
    param = {}
    version = '20210327062642'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def DeleteRule(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/deleteRule'
    head = {}
    param = {}
    version = '20210327062626'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数不可以为空
#  描述:
#参数productId: 类型String, 参数可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def GetRules(appKey, appSecret, ruleId, productId, pageNow, pageSize):
    path = '/aep_rule_engine/v3/rule/getRules'
    head = {}
    param = {'ruleId':ruleId, 'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20210327062616'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def GetRuleRunStatus(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/getRuleRunningStatus'
    head = {}
    param = {}
    version = '20210327062610'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateRuleRunStatus(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/modifyRuleRunningStatus'
    head = {}
    param = {}
    version = '20210327062603'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateForward(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/addForward'
    head = {}
    param = {}
    version = '20210327062556'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateForward(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/updateForward'
    head = {}
    param = {}
    version = '20210327062549'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def DeleteForward(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/deleteForward'
    head = {}
    param = {}
    version = '20210327062539'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数不可以为空
#  描述:
#参数productId: 类型String, 参数可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def GetForwards(appKey, appSecret, ruleId, productId, pageNow, pageSize):
    path = '/aep_rule_engine/v3/rule/getForwards'
    head = {}
    param = {'ruleId':ruleId, 'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20210327062531'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数不可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def GetWarns(appKey, appSecret, ruleId, pageNow, pageSize):
    path = '/aep_rule_engine/v3/rule/getWarns'
    head = {}
    param = {'ruleId':ruleId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20210423162903'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def DeleteWarn(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/deleteWarn'
    head = {}
    param = {}
    version = '20210423162859'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateWarn(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/updateWarn'
    head = {}
    param = {}
    version = '20210423162906'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateWarn(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/addWarn'
    head = {}
    param = {}
    version = '20210423162909'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateAction(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/addAction'
    head = {}
    param = {}
    version = '20210423162837'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateAction(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/updateAction'
    head = {}
    param = {}
    version = '20210423162842'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def DeleteAction(appKey, appSecret, body):
    path = '/aep_rule_engine/v3/rule/deleteAct'
    head = {}
    param = {}
    version = '20210423162848'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数不可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def GetActions(appKey, appSecret, ruleId, pageNow, pageSize):
    path = '/aep_rule_engine/v3/rule/getActions'
    head = {}
    param = {'ruleId':ruleId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20211028100156'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def GetWarnUsers(appKey, appSecret, pageNow, pageSize):
    path = '/aep_rule_engine/v3/rule/getWarnUsers'
    head = {}
    param = {'pageNow':pageNow, 'pageSize':pageSize}
    version = '20210423162830'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

