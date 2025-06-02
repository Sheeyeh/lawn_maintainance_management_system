from handler import login_handler

"""
登陆校验
"""


def login(request):
    params = request.body
    if not params or "code" not in params:
        raise Exception("入参有误")

    code = params["code"]
    data = login_handler.LoginHandler.login(code)
    return data


def register(request):
    user_id = request.user_id
    params = request.body
    user_account = params["user_account"]
    user_address = params["user_address"]
    phone_num = params["phone_num"]
    user_district = params["user_district"]

    if not params:
        raise Exception("入参有误")

    if login_handler.LoginHandler.register(user_id, user_account, user_address, phone_num, user_district):
        return {"isRegistered": True, "msg": "注册成功"}
    else:
        return {"isRegistered": False, "msg": "注册失败"}


def clerkLogin(request):
    params = request.body
    if not params or "code" not in params:
        raise Exception("入参有误")

    code = params["code"]
    data = login_handler.LoginHandler.clerkLogin(code)
    return data


def clerkRegister(request):
    clerk_id = request.user_id
    params = request.body
    clerk_account = params["clerk_account"]
    clerk_phone_num = params["clerk_phone_num"]
    clerk_email = params["clerk_email"]
    clerk_name = params["clerk_name"]

    if not params:
        raise Exception("入参有误")

    if login_handler.LoginHandler.clerkRegister(clerk_id, clerk_account, clerk_phone_num, clerk_email, clerk_name):
        return {"isRegistered": True, "msg": "注册成功"}
    else:
        return {"isRegistered": False, "msg": "注册失败"}
