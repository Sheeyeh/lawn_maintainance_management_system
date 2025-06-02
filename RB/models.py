from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_district = models.CharField(max_length=50, null=True, default="default")
    user_address = models.CharField(max_length=50, null=True, default="default")
    user_account = models.CharField(max_length=50, null=True, default="default")
    user_change = models.FloatField(null=True, default=0)
    user_credit = models.FloatField(null=True, default=0)
    phone_num = models.CharField(max_length=50, null=True)
    dev_id = models.CharField(max_length=50, null=True)
    register_time = models.DateTimeField(null=True)
    isRegister = models.BooleanField(default=False)
    user_status = models.IntegerField(null=True, default=0)
    del_flag = models.BooleanField(default=False)


class Clerk(models.Model):
    clerk_id = models.CharField(max_length=50)
    clerk_account = models.CharField(max_length=50, null=True, default="default")
    clerk_name = models.CharField(max_length=50, null=True, default="default")
    clerk_phone_num = models.CharField(max_length=50, null=True)
    clerk_change = models.FloatField(null=True, default=0)
    clerk_register_time = models.DateTimeField(null=True)
    clerk_email = models.CharField(max_length=50, null=True)
    clerk_update_time = models.DateTimeField(null=True)
    clerk_status = models.BooleanField(null=True, default=False)
    clerk_register = models.BooleanField(default=False)
    del_flag = models.BooleanField(default=False)


class Device(models.Model):
    dev_id = models.CharField(max_length=50)
    dev_user_id = models.CharField(max_length=50, null=True)
    dev_address = models.CharField(max_length=50, null=True)
    dev_height = models.FloatField(null=True)
    dev_battery = models.FloatField(null=True)
    dev_create_time = models.DateTimeField(null=True)
    dev_update_time = models.DateTimeField(null=True)
    dev_duration = models.IntegerField(null=True, default=0)
    dev_status = models.IntegerField(default=1)
    del_flag = models.BooleanField(default=False)


class Order(models.Model):
    order_id = models.CharField(max_length=50)
    order_user_id = models.CharField(max_length=50)
    order_clerk_id = models.CharField(max_length=50, null=True)
    order_tag = models.BooleanField(null=True)
    order_price = models.FloatField(null=True)
    order_status = models.IntegerField(null=True)
    order_memo = models.CharField(max_length=100, null=True)
    order_address = models.CharField(max_length=50, null=True)
    order_create_time = models.DateTimeField(null=True)
    order_update_time = models.DateTimeField(null=True)
    order_finish_time = models.DateTimeField(null=True)
    order_remark = models.IntegerField(null=True, default=0)
    del_flag = models.BooleanField(default=False)


# Create your models here.
class Repair(models.Model):
    repair_id = models.CharField(max_length=50, null=True)
    repair_user_id = models.CharField(max_length=50, null=True)
    # 报修内容
    repair_memo = models.CharField(max_length=100, null=True)
    # 报修状态 0为未处理 1为已处理
    repair_status = models.IntegerField(default=0)
    repair_photo = models.CharField(max_length=100, null=True)
    repair_create_time = models.DateTimeField(null=True)
    del_flag = models.BooleanField(default=False)
