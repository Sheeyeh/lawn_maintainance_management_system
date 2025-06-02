from RB import models
import datetime


class UserHandler:
    @staticmethod
    def queryUserInfo(user_id):
        try:
            obj = models.User.objects.get(user_id=user_id)

        except:
            data = False

            return data
        data = {
            "user_account": obj.user_account,
            "user_address": obj.user_address,
            "phone_num": obj.phone_num,
            "user_district": obj.user_district
        }
        return data

    @staticmethod
    def changeUserInfoHandler(user_id, user_account, user_address, phone_num, user_district):
        try:

            models.User.objects.filter(user_id=user_id, del_flag=0).update(user_account=user_account,
                                                                           user_address=user_address,
                                                                           phone_num=phone_num,
                                                                           user_district=user_district)
        except:
            data = False
            return data

        data = True
        return data

    @staticmethod
    def addDeviceHandler(user_id, dev_id):
        user = models.User.objects.get(user_id=user_id)
        user.dev_id = dev_id
        user.save()
        try:
            query = models.Device.objects.get(dev_user_id=user_id)
            return False
        except:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            models.Device.objects.create(dev_id=dev_id, dev_user_id=user_id, dev_address=user.user_address,
                                         dev_status=1, dev_create_time=formatted_time)
            return True
