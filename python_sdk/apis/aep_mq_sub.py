#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



def QueryServiceState(appKey, appSecret):
    path = '/aep_mq_sub/mqStat'
    head = {}
    param = {}
    version = '20201218144210'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def OpenMqService(appKey, appSecret, body):
    path = '/aep_mq_sub/mqStat'
    head = {}
    param = {}
    version = '20201217094438'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateTopic(appKey, appSecret, body):
    path = '/aep_mq_sub/topic'
    head = {}
    param = {}
    version = '20201218142343'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数topicId: 类型long, 参数不可以为空
#  描述:
def QueryTopicInfo(appKey, appSecret, topicId):
    path = '/aep_mq_sub/topic'
    head = {}
    param = {'topicId':topicId}
    version = '20201218153403'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数topicId: 类型long, 参数不可以为空
#  描述:
def QueryTopicCacheInfo(appKey, appSecret, topicId):
    path = '/aep_mq_sub/topic/cache'
    head = {}
    param = {'topicId':topicId}
    version = '20201218150354'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

def QueryTopics(appKey, appSecret):
    path = '/aep_mq_sub/topics'
    head = {}
    param = {}
    version = '20201218153456'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数topicId: 类型long, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ChangeTopicInfo(appKey, appSecret, topicId, body):
    path = '/aep_mq_sub/topic'
    head = {}
    param = {'topicId':topicId}
    version = '20201218153044'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def QuerySubRules(appKey, appSecret, body):
    path = '/aep_mq_sub/rule'
    head = {}
    param = {}
    version = '20201218160237'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ChangeSubRules(appKey, appSecret, body):
    path = '/aep_mq_sub/rule'
    head = {}
    param = {}
    version = '20201218161013'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'PUT')
    if response is not None:
        return response.read()
    return None

def ClosePushService(appKey, appSecret):
    path = '/aep_mq_sub/mqStat'
    head = {}
    param = {}
    version = '20201217141937'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

