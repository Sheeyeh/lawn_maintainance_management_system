import django.core.exceptions
from RB import models
import datetime


# clerk数据库处理器

class ClerkHandler:
    @staticmethod
    def queryOrderListByStatus():
        # 根据订单状态查询订单
        # def queryOrderListByStatus(order_status):
        order_list = []
        # querySet = models.Order.objects.filter(order_status=order_status, del_flag=0)
        querySet = models.Order.objects.filter(order_clerk_id=None, del_flag=0)
        for obj in querySet:
            order_data = {
                "order_id": obj.order_id,
                "order_address": obj.order_address,
                "order_status": obj.order_status,
                "order_price": obj.order_price,
                "order_tag": obj.order_tag,
                "order_create_time": obj.order_create_time.timestamp()
            }
            order_list.append(order_data)

        return order_list

    @staticmethod
    def clerkChangesQueryHandler(user_id):
        # 员工零钱查询
        query = models.Clerk.objects.get(clerk_id=user_id, del_flag=0)
        data = {"changes": query.clerk_change}
        return data

    @staticmethod
    def changeClerkInfoHandler(clerk_id, clerk_account, clerk_phone_num, clerk_email, clerk_name):
        # 修改员工信息
        models.Clerk.objects.filter(clerk_id=clerk_id, del_flag=0).update(clerk_phone_num=clerk_phone_num,
                                                                          clerk_account=clerk_account,
                                                                          clerk_email=clerk_email,
                                                                          clerk_name=clerk_name)
        data = True
        return data

    @staticmethod
    def clerkInfoQueryHandler(clerk_id):
        # 员工信息查询
        query = models.Clerk.objects.get(clerk_id=clerk_id)
        data = {
            "clerk_name": query.clerk_name,
            "clerk_account": query.clerk_account,
            "clerk_email": query.clerk_email,
            "clerk_phone_num": query.clerk_phone_num,
            "clerk_status": query.clerk_status
        }
        return data

    @staticmethod
    def queryOrderByClerkIdHandler(clerk_id):
        # 查询员工订单
        order_list = []
        querySet = models.Order.objects.filter(order_clerk_id=clerk_id, del_flag=0)
        for obj in querySet:
            order_data = {
                "order_id": obj.order_id,
                "order_address": obj.order_address,
                "order_status": obj.order_status,
                "order_remark": obj.order_remark,
                "order_price": obj.order_price,
                "order_tag": obj.order_tag,
                "order_create_time": obj.order_create_time.timestamp(),
                "order_update_time": "" if not obj.order_update_time else obj.order_update_time.timestamp(),
                "order_finish_time": "" if not obj.order_finish_time else obj.order_finish_time.timestamp()
            }
            order_list.append(order_data)
        return order_list

    @staticmethod
    def receiveOrderHandler(clerk_id, order_id):
        # 接取订单
        # models.Order.objects.filter(order_id=order_id,order_status=1,del_flag=0).update(clerk_id=clerk_id,order_status=2)
        try:
            query = models.Order.objects.get(order_id=order_id, order_status=1, del_flag=0)
        except:
            return "订单不存在"
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        query.order_clerk_id = clerk_id
        query.order_status = 2
        query.order_update_time = formatted_time
        query.save()
        return True

    @staticmethod
    def receiveAutoOrderHandler(clerk_id, order_id):
        # 自动接取订单
        # models.Order.objects.filter(order_id=order_id,order_status=1,del_flag=0).update(clerk_id=clerk_id,order_status=2)
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        query = models.Order.objects.get(order_id=order_id, order_status=7, del_flag=0)
        query.order_clerk_id = clerk_id
        query.order_status = 8
        query.order_update_time = formatted_time
        query.save()
        return True

    @staticmethod
    def qualifyClerkHandler(clerk_id):
        # 修改员工状态
        models.Clerk.objects.filter(clerk_id=clerk_id, clerk_status=0, del_flag=0).update(clerk_status=1)
        data = True
        return data

    @staticmethod
    def clerkMinusChangesHandler(clerk_id, clerk_change):
        # 员工零钱提现
        query = models.Clerk.objects.get(clerk_id=clerk_id, del_flag=0)
        if query.clerk_change - clerk_change < 0:
            return -1
        query.clerk_change = query.clerk_change - clerk_change
        query.save()
        return query.clerk_change

    @staticmethod
    def clerkAddChangesHandler(clerk_id, clerk_change):
        # 员工零钱充值
        query = models.Clerk.objects.get(clerk_id=clerk_id, del_flag=0)
        query.clerk_change = query.clerk_change + clerk_change
        query.save()
        return query.clerk_change

    @staticmethod
    def clerkFinishOrderHandler(order_id):
        # 完成订单
        try:
            query = models.Order.objects.get(order_id=order_id, order_status=2, del_flag=0)
        except:
            return -1
        clerk_id = query.order_clerk_id
        reward = 0.7 * query.order_price
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        clerk = models.Clerk.objects.get(clerk_id=clerk_id, del_flag=0)
        print(clerk.clerk_change)
        data = ClerkHandler.clerkAddChangesHandler(clerk_id, round(reward, 2))
        print(data)
        models.Order.objects.filter(order_id=order_id, order_status=2, del_flag=0).update(order_status=3,
                                                                                          order_finish_time=formatted_time)
        return True

    @staticmethod
    def clerkAutoFinishOrderHandler(order_id, order_price):
        # 自动完成订单
        try:
            query = models.Order.objects.filter(order_id=order_id, order_status=8, del_flag=0).last()
        except:
            return -1
        clerk_id = query.order_clerk_id
        reward = 0.7 * order_price
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        clerk = models.Clerk.objects.get(clerk_id=clerk_id, del_flag=0)
        print(clerk.clerk_change)
        data = ClerkHandler.clerkAddChangesHandler(clerk_id, round(reward, 2))
        print(data)
        models.Order.objects.filter(order_id=order_id, order_status=8, del_flag=0).update(order_status=9,
                                                                                          order_finish_time=formatted_time)
        return True

    @staticmethod
    def clerkIsQualifiedHandler(clerk_id):
        # 员工状态查询
        query = models.Clerk.objects.get(clerk_id=clerk_id)
        if query.clerk_status:
            return True
        return False

    @staticmethod
    def clerkChangeBatteryHandler(clerk_id, dev_id):
        # 更换电池接单
        device_query = models.Device.objects.filter(dev_id=dev_id).last()
        user_id = device_query.dev_user_id
        order_query = models.Order.objects.filter(order_user_id=user_id, order_status=10, del_flag=0).last()

        if not order_query:
            return "记录不存在"

        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        order_query.order_status = 11
        order_query.order_clerk_id = clerk_id
        order_query.order_update_time = formatted_time
        order_query.save()
        return True

    @staticmethod
    def clerkFinishBatteryHandler(clerk_id, dev_id):
        # 更换电池完成
        device_query = models.Device.objects.filter(dev_id=dev_id).last()
        user_id = device_query.dev_user_id
        print(user_id)
        order_query = models.Order.objects.filter(order_user_id=user_id, order_status=11, del_flag=0).last()
        if not order_query:
            print(111)
            return "记录不存在"
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        order_query.order_status = 12
        order_query.order_clerk_id = clerk_id
        order_query.order_finish_time = formatted_time
        order_query.save()
        device_query.dev_status = 1
        device_query.save()
        return True
