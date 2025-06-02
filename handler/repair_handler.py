from RB import models
import uuid
from datetime import datetime


class RepairHandler:
    @staticmethod
    def placeRepairRecordHandler(repair_user_id, repair_memo, repair_photo):
        #  def placeOrderHandler(order_user_id, order_address, order_tag, order_price):
        #     if OrderHandler.minusChangeHandler(order_user_id, order_price) == -1:
        #         return -1
        repair_id = uuid.uuid4()
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        #     # 创建订单记录
        obj = models.Repair(repair_user_id=repair_user_id, repair_id=repair_id,
                            repair_status=0, repair_create_time=formatted_time,
                            repair_memo=repair_memo, repair_photo=repair_photo)
        obj.save()
        return obj

    #     obj.save()

    #     query = models.Order.objects.get(del_flag=0, order_id=order_id)
    #     if str(order_id) != query.order_id:
    #         return None

    #     return order_id

    @staticmethod
    def queryRepairListHandler(user_id):
        repair_list = []
        querySet = models.Repair.objects.filter(repair_user_id=user_id)
        if not querySet.exists():
            return repair_list
        for record in list(querySet):
            repair_data = {'repair_id': record.repair_id, 'repair_create_time': record.repair_create_time.timestamp(),
                           'repair_status': record.repair_status}
            repair_list.append(repair_data)
        return repair_list

    @staticmethod
    def queryRepairDataHandler():
        repair_list = []
        querySet = models.Repair.objects.all()
        if not querySet.exists():
            return repair_list
        for record in list(querySet):
            repair_data = {'repair_id': record.repair_id, 'repair_create_time': record.repair_create_time.timestamp(),
                           'repair_status': record.repair_status, 'repair_photo': record.repair_photo}
            repair_list.append(repair_data)
        data = {"data": repair_list}
        return data

    @staticmethod
    def queryRepairDetail(repair_id):
        query = {}
        obj = models.Repair.objects.get(repair_id=repair_id)
        query['repair_create_time'] = obj.repair_create_time.timestamp()
        query['repair_status'] = obj.repair_status
        query['repair_memo'] = obj.repair_memo
        query['repair_photo'] = obj.repair_photo
        return query

    @staticmethod
    def changeRepairStatusHandler(repair_id,repair_status):
        models.Repair.objects.filter(repair_id=repair_id, del_flag=0).update(repair_status=1)
        return True
