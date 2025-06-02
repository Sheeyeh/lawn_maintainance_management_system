from handler import user_handler, device_handler


def queryUserInfo(request):
    user_id = request.user_id
    data = user_handler.UserHandler.queryUserInfo(user_id)

    return data


def changeUserInfo(request):
    user_id = request.user_id
    params = request.body.get("data")
    user_account = params["user_account"]
    user_address = params["user_address"]
    phone_num = params["phone_num"]
    user_district=params["user_district"]
    data = user_handler.UserHandler.changeUserInfoHandler(user_id, user_account, user_address, phone_num,user_district)
    return data


def addDevice(request):
    user_id = request.user_id
    device_list = device_handler.DeviceHandler.queryDeviceHandler()
    dev_id = device_list["devID"]
    data = user_handler.UserHandler.addDeviceHandler(user_id, dev_id)
    return data
