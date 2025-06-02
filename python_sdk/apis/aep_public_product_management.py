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
def QueryPublicByPublicProductId(appKey, appSecret, body):
    path = '/aep_public_product_management/publicProducts'
    head = {}
    param = {}
    version = '20190507003930'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def QueryPublicByProductId(appKey, appSecret, body):
    path = '/aep_public_product_management/publicProductList'
    head = {}
    param = {}
    version = '20190507004139'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def InstantiateProduct(appKey, appSecret, body):
    path = '/aep_public_product_management/instantiateProduct'
    head = {}
    param = {}
    version = '20200801233037'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数searchValue: 类型String, 参数可以为空
#  描述:设备类型、厂商ID、厂商名称
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
def QueryAllPublicProductList(appKey, appSecret, searchValue, pageNow, pageSize):
    path = '/aep_public_product_management/allPublicProductList'
    head = {}
    param = {'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200829005548'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数searchValue: 类型String, 参数可以为空
#  描述:产品名称
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
#参数productIds: 类型String, 参数可以为空
#  描述:私有产品idList
def QueryMyPublicProductList(appKey, appSecret, searchValue, pageNow, pageSize, productIds):
    path = '/aep_public_product_management/myPublicProductList'
    head = {}
    param = {'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize, 'productIds':productIds}
    version = '20200829005359'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

