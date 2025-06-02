from datetime import datetime
from RB import models
from handler import basic_handler
import uuid


class OrderHandler:
    @staticmethod
    def changeQueryHandler(user_id):
        query = models.User.objects.get(user_id=user_id, del_flag=0)
        if not query:
            return query
        data = {"change": query.user_change}
        return data

    @staticmethod
    def queryOrderListByUserHandler(user_id):
        # 根据用户id查询用户对应订单实现方法
        order_list = []

        # 从数据库中查找订单用户id与要查找的用户id相等，且订单状态在1-9之间的未删除数据
        querySet = models.Order.objects.filter(order_user_id=user_id, order_status__range=[1, 9], del_flag=0)

        if not querySet.exists():
            return order_list

        # 遍历数据库记录，以列表的形式取出数据
        for record in list(querySet):
            if record.order_clerk_id:
                clerk_id = record.order_clerk_id
                clerk = models.Clerk.objects.get(clerk_id=clerk_id)
                clerk_name = clerk.clerk_name
            else:
                clerk_name = "无"
            order_data = {'order_create_time': record.order_create_time.timestamp(), 'order_id': record.order_id,
                          'order_tag': record.order_tag, 'order_status': record.order_status,
                          'order_price': record.order_price, 'order_clerk_id': clerk_name,
                          'order_remark': record.order_remark}
            order_list.append(order_data)
        # 返回数据给数据处理函数
        return order_list

    @staticmethod
    def queryAutoOrderListByUser(user_id):
        order_list = []
        querySet = models.Order.objects.filter(order_user_id=user_id, order_status__range=[10, 12], del_flag=0)
        if not querySet.exists():
            return order_list

        for record in list(querySet):
            if record.order_clerk_id:
                clerk_id = record.order_clerk_id
                clerk = models.Clerk.objects.get(clerk_id=clerk_id)
                clerk_name = clerk.clerk_name
            else:
                clerk_name = "无"
            order_data = {'order_create_time': record.order_create_time.timestamp(), 'order_id': record.order_id,
                          'order_tag': record.order_tag, 'order_status': record.order_status,
                          'order_price': record.order_price, 'order_clerk_id': clerk_name,
                          'order_remark': record.order_remark}
            order_list.append(order_data)
        return order_list

    # @staticmethod
    # def queryPackageListByUser(user_id):
    #     order_list = []
    #     querySet = models.Order.objects.filter(order_user_id=user_id, del_flag=0, order_status=4)
    #     if not querySet.exists():
    #         return order_list

    #     for record in list(querySet):
    #         order_data = {'order_create_time': record.order_create_time.timestamp(), 'order_id': record.order_id,
    #                       'order_tag': record.order_tag, 'order_status': record.order_status,
    #                       'order_price': record.order_price, 'order_clerk_id': record.order_clerk_id}
    #         order_list.append(order_data)

    #     return order_list

    @staticmethod
    def placeOrderHandler(order_user_id, order_address, order_tag, order_price, order_status=1):
        if OrderHandler.minusChangeHandler(order_user_id, order_price) == -1:
            return -1
        order_id = uuid.uuid4()
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # 创建订单记录
        obj = models.Order(order_user_id=order_user_id, order_id=order_id, order_address=order_address,
                           order_status=order_status, order_create_time=formatted_time,
                           order_tag=order_tag, order_price=order_price, del_flag=0)
        obj.save()

        query = models.Order.objects.get(del_flag=0, order_id=order_id)
        if str(order_id) != query.order_id:
            return None

        return order_id

    @staticmethod
    def addChangeHandler(user_id, add_change):

        query = models.User.objects.get(user_id=user_id, del_flag=0)
        query.user_change = query.user_change + add_change
        query.save()
        print(query.user_change)
        return query.user_change

    @staticmethod
    def minusChangeHandler(user_id, minus_change):
        query = models.User.objects.get(user_id=user_id, del_flag=0)
        print(query.user_change)
        if query.user_change - minus_change >= 0:
            query.user_change = query.user_change - minus_change
            query.save()
            return query.user_change
        else:
            # 余额不足，请充值
            return -1

    @staticmethod
    def queryOrderByOrderIdHandler(order_id):
        query = models.Order.objects.get(order_id=order_id)
        print(query.order_id)
        clerk_id = query.order_clerk_id
        if clerk_id is None:
            clerk = "暂时无人接单"
        else:
            clerk = models.Clerk.objects.get(clerk_id=clerk_id).clerk_name

        data = {
            "order_clerk_id": clerk,
            "order_tag": query.order_tag,
            "order_price": query.order_price,
            "order_status": query.order_status,
            "order_remark": query.order_remark,
            "order_address": query.order_address,
            "order_create_time": query.order_create_time.timestamp(),
            "order_update_time": "" if not query.order_update_time else query.order_update_time.timestamp(),
            "order_finish_time": "" if not query.order_finish_time else query.order_finish_time.timestamp()
        }
        return data

    @staticmethod
    def createOrderRemarkHandler(order_id, order_remark):
        models.Order.objects.filter(order_id=order_id).update(order_remark=order_remark)
        return models.Order.objects.get(order_id=order_id).order_remark

    @staticmethod
    def orderPackageHandler(order_user_id, order_address, order_tag, package_type):
        print(order_tag, package_type)
        package_list = [
            [9.9, 32.8, 88.8, 358],
            [5.5, 19.8, 48.8, 198],
            [7, 30, 90, 365]
        ]

        order_price = package_list[order_tag][package_type]
        if OrderHandler.minusChangeHandler(order_user_id, order_price) == -1:
            return -1
        order_id = uuid.uuid4()
        now = datetime.now()
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')
        dev_duration = 86400 * package_list[2][package_type]
        finish = now.timestamp() + 86400 * package_list[2][package_type]
        finish_time = basic_handler.TimeHandler.timestampHandler(finish)
        # if models.Order.objects.filter(order_user_id=order_user_id,order_status=4,del_flag=0).exists():
        #     models.Order.objects.filter(order_user_id=order_user_id,order_status=4,del_flag=0).update()
        models.Order.objects.create(order_id=order_id, order_user_id=order_user_id, order_price=order_price,
                                    order_address=order_address, order_tag=order_tag, order_status=4,
                                    order_create_time=current_time, order_finish_time=finish_time,
                                    order_update_time=current_time)
        models.Device.objects.filter(dev_user_id=order_user_id).update(dev_duration=dev_duration)
        return order_id

    @staticmethod
    def packageQueryHandler(order_user_id):
        query = models.Order.objects.filter(order_user_id=order_user_id, order_status=4, del_flag=0).last()
        current_time = datetime.now().timestamp()
        if query:
            if current_time > query.order_finish_time.timestamp():
                isFinished = True
            else:
                isFinished = False
        else:
            isFinished = True
        data = {
            "order_create_time": "" if not query else query.order_create_time.timestamp(),
            "order_finish_time": "" if not query else query.order_finish_time.timestamp(),
            "order_tag": "" if not query else query.order_tag,
            "isFinished": isFinished
        }

        return data
