import requests
from RB import models
from handler import basic_handler
import datetime
from rubbishBin import settings
from rubbishBin.utils.jwt import create_token

#登录处理器

class LoginHandler:
    @staticmethod
    def login(code):
    #登录函数
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(settings.APP_ID, settings.APP_KEY, code)
        res = requests.get(url)
        try:
            openid = res.json()['openid']
            session_key = res.json()['session_key']
        except:
            data = {'message': '微信调用失败', 'token': ''}
            return data

        if not models.User.objects.filter(user_id=openid, del_flag=0):
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            models.User.objects.create(user_id=openid, register_time=formatted_time)
        if not LoginHandler.isRegistered(openid):
            data = {'message': '用户未注册', 'token': create_token(openid), 'isRegistered': False}
            return data

        data = {"token": create_token(openid), 'isRegistered': True}
        return data

    @staticmethod
    def isRegistered(openid):
        #判断是否注册
        if models.User.objects.get(user_id=openid, del_flag=0).isRegister:
            return True
        return False

    @staticmethod
    def register(user_id, user_account, user_address, phone_num, user_district):
        #注册函数
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        models.User.objects.filter(user_id=user_id).update(user_account=user_account, user_address=user_address,
                                                           user_change=0,
                                                           user_credit=0, phone_num=phone_num,
                                                           register_time=formatted_time, isRegister=1,
                                                           user_district=user_district)

        return LoginHandler.isRegistered(user_id)

    @staticmethod
    def clerkLogin(code):
        #员工登录函数
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(settings.APP_ID, settings.APP_KEY, code)
        res = requests.get(url)
        try:
            openid = res.json()['openid']
            session_key = res.json()['session_key']
        except:
            data = {'message': '微信调用失败', 'token': ''}
            return data

        if not models.Clerk.objects.filter(clerk_id=openid, del_flag=0):
            # 如果该id未注册
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            models.Clerk.objects.create(clerk_id=openid, clerk_register_time=formatted_time)
            # 把id存进数据库

        if not LoginHandler.clerkIsRegistered(openid):
            # 如果该id未注册，返回消息
            data = {'message': '用户未注册', 'token': create_token(openid), 'isRegistered': False}
            return data

        data = {"token": create_token(openid), 'isRegistered': True}
        return data

    @staticmethod
    def clerkIsRegistered(openid):
        # 判断是否注册
        if models.Clerk.objects.get(clerk_id=openid, del_flag=0).clerk_register:
            return True
        return False

    @staticmethod
    def clerkRegister(clerk_id, clerk_account, clerk_phone_num, clerk_email, clerk_name):
        #员工注册函数
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        models.Clerk.objects.filter(clerk_id=clerk_id).update(clerk_account=clerk_account,
                                                              clerk_change=0, clerk_phone_num=clerk_phone_num,
                                                              clerk_email=clerk_email,
                                                              clerk_register_time=formatted_time, clerk_register=1,
                                                              clerk_name=clerk_name)

        return LoginHandler.clerkIsRegistered(clerk_id)
