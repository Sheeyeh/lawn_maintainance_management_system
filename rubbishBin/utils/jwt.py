import jwt
import datetime
from jwt import exceptions
 
# 加的盐
JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"
 
def create_token(user_id,timeout=60):
    # 声明类型，声明加密算法
    headers = {
        "type":"jwt",
        "alg":"HS256"
    }
    payload = {}
    payload['user_id'] = user_id
    # 设置过期时间
    payload['exp'] = datetime.datetime.now() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload,key=JWT_SALT,algorithm="HS256",headers=headers)
    # 返回加密结果
    return result
 
 
def parse_payload(token):
    """
    用于解密
    :param token:
    :return:
    """
    result = {"status":False,"data":None,"error":None}
    try:
        # 进行解密
        verified_payload = jwt.decode(token,JWT_SALT,"HS256")
        result["status"] = True
        result['data']= verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result
 