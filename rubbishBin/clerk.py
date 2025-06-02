import logging

from handler import clerk_handler, device_handler


def queryOrderListByStatus(request):
    # params = request.body.get("data")
    # params=request.body
    # order_status = params["order_status"]
    order_list = clerk_handler.ClerkHandler.queryOrderListByStatus()
    return order_list


def clerkChangesQuery(request):
    user_id = request.user_id
    data = clerk_handler.ClerkHandler.clerkChangesQueryHandler(user_id)
    return data


def changeClerkInfo(request):
    clerk_id = request.user_id
    params = request.body.get("data")
    # params=request.body
    clerk_account = params["clerk_account"]
    clerk_phone_num = params["clerk_phone_num"]
    clerk_email = params["clerk_email"]
    clerk_name = params["clerk_name"]
    data = clerk_handler.ClerkHandler.changeClerkInfoHandler(clerk_id, clerk_account, clerk_phone_num, clerk_email,
                                                             clerk_name)
    return data


def clerkInfoQuery(request):
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.clerkInfoQueryHandler(clerk_id)
    return data


def queryOrderByClerkId(request):
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.queryOrderByClerkIdHandler(clerk_id)
    return data


def receiveOrder(request):
    # params=request.body
    params = request.body.get("data")
    order_id = params["order_id"]
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.receiveOrderHandler(clerk_id, order_id)
    return data


def receiveAutoOrder(request):
    # params=request.body
    params = request.body.get("data")
    order_id = params["order_id"]
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.receiveAutoOrderHandler(clerk_id, order_id)
    return data


def qualifyClerk(request):
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.qualifyClerkHandler(clerk_id)
    return data


def clerkMinusChanges(request):
    clerk_id = request.user_id
    params = request.body.get("data")
    clerk_change = params["clerk_change"]
    data = clerk_handler.ClerkHandler.clerkMinusChangesHandler(clerk_id, clerk_change)
    return data


def clerkAddChanges(request):
    clerk_id = request.user_id
    params = request.body.get("data")
    clerk_change = params["clerk_change"]
    data = clerk_handler.ClerkHandler.clerkAddChangesHandler(clerk_id, clerk_change)
    return data


def clerkFinishOrder(request):
    params = request.body.get("data")
    order_id = params["order_id"]
    data = clerk_handler.ClerkHandler.clerkFinishOrderHandler(order_id)
    return data


def clerkIsQualified(request):
    clerk_id = request.user_id
    data = clerk_handler.ClerkHandler.clerkIsQualifiedHandler(clerk_id)
    return data


def clerkChangeBattery(request):
    clerk_id = request.user_id
    device_list = device_handler.DeviceHandler.queryDeviceHandler()
    dev_id = device_list["devID"]
    data = clerk_handler.ClerkHandler.clerkChangeBatteryHandler(clerk_id, dev_id)
    return data


def clerkFinishBattery(request):
    clerk_id = request.user_id
    device_list = device_handler.DeviceHandler.queryDeviceHandler()
    dev_id = device_list["devID"]
    data = clerk_handler.ClerkHandler.clerkFinishBatteryHandler(clerk_id, dev_id)
    return data
