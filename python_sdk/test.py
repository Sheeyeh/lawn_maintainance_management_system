import base64
from apis.aep_device_status import QueryDeviceStatusList

# 接收数据，最后要存在一个文件里
appKey = 'vKQUt3OMKAh'
appSecret = 'uIGFrBQLG1'
body = '{"productId": "15285641",'' "deviceId": "%s",'' "datasetId": "APPdata"}'
deviceid = 1528564111
result = QueryDeviceStatusList(appKey, appSecret, body % deviceid)

# 取出deviceStatusList
dict1 = eval(result)  # result为字符串，转化为字典
dsl = dict1["deviceStatusList"][0]  # 取出deviceStatusList的值，值为列表，转化为字典
value = dsl["value"]  # 取出其中的信息，准备base64解码
re = base64.b64decode(value)  # base64解码
device_list = eval(re)  # 解码结果为字符串，转化为字典

# 打印结果
print()
print(result)
print("##########################")
print(device_list)
# print(test.decode(encoding='utf8'))  # 解码desc
# print(desc["desc"])
# 返回的desc是一串uft8的编码：
# （"\xe6\x9c\xaa\xe8\x8e\xb7\xe5\x8f\x96\xe5\x88\xb0\xe8
#   \xae\xbe\xe5\xa4\x87\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a
#   \xb6\xe6\x80\x81\xe5\x88\x97\xe8\xa1\xa8\xef\xbc\x81"）
