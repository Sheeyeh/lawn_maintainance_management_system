from RB import models
from handler import order_handler, clerk_handler
import base64
import uuid
from python_sdk.apis.aep_device_status import QueryDeviceStatusList
from datetime import datetime


# device数据库处理器
class DeviceHandler:
    @staticmethod
    def queryDeviceHandler():
        # 查询设备数据
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
        return device_list

    @staticmethod
    def autoOrderByHeightHandler(dev_id):
        # 自动获取高度信息，并判断是否下单和完成
        result = {"order_id": "", "height": None, "isClean": False}
        query = models.Device.objects.filter(dev_id=dev_id).last()
        user_id = query.dev_user_id
        old_height = query.dev_height
        print("old_height:", old_height)

        device_list = DeviceHandler.queryDeviceHandler()
        new_height = 156 - int(device_list["height"])
        # new_height = 0
        print("new_height:", new_height)

        order_address = models.User.objects.get(user_id=user_id).user_address
        data = order_handler.OrderHandler.packageQueryHandler(user_id)

        if not data["isFinished"] and new_height < 155:
            print("接受高度正常")
            if new_height > int(old_height) + 5 and new_height > 5:
                query.dev_height = new_height
                query.save()
                result["order_id"] = order_handler.OrderHandler.placeOrderHandler(user_id, order_address,
                                                                                  data["order_tag"], 0, 7)
                result["height"] = new_height
                print(">>>>>")
                return result

            if new_height < int(old_height) - 5:
                query.dev_height = new_height
                query.save()
                order_id = models.Order.objects.filter(order_user_id=user_id, order_status=8,
                                                       del_flag=0).last().order_id
                print(order_id)
                if data["order_tag"]:
                    order_price = 1
                else:
                    order_price = 2
                print(order_price)
                isClean = clerk_handler.ClerkHandler.clerkAutoFinishOrderHandler(order_id, order_price)

                result["height"] = new_height
                result["isClean"] = isClean
                print("<<<<<<<<")
                return result
            print("高度保持不变")
        query.dev_height = new_height
        query.save()

        result["height"] = new_height
        return result

    @staticmethod
    def autoBatteryHandler(dev_id):
        # 获取电池信息并判断是否下单
        device_list = DeviceHandler.queryDeviceHandler()
        battery = device_list["battery"]

        print("battery:", battery)

        query = models.Device.objects.filter(dev_id=dev_id).last()
        user_id = query.dev_user_id
        dev_status = query.dev_status
        order_address = models.User.objects.get(user_id=user_id).user_address
        if dev_status == 1:
            print("电池电量接受正常")
            if int(battery) < 10700:
                query.dev_status = -1
                query.save()
                order_id = uuid.uuid4()
                now = datetime.now()
                current_time = now.strftime('%Y-%m-%d %H:%M:%S')
                models.Order.objects.create(order_id=order_id, order_user_id=user_id, order_price=1,
                                            order_address=order_address, order_tag=0, order_status=10,
                                            order_create_time=current_time)
                return order_id

        return "正常"
