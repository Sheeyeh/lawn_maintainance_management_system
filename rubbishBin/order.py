from handler import order_handler


def changesQuery(request):
    user_id = request.user_id
    data = order_handler.OrderHandler.changeQueryHandler(user_id)
    return data


def queryOrderListByUser(request):
    # 根据用户id查询用户对应订单
    user_id = request.user_id

    if not user_id:
        raise Exception("入参有误")

    order_list = order_handler.OrderHandler.queryOrderListByUserHandler(user_id)

    if order_list is None:
        raise Exception("查询列表为空")

    return order_list


def queryAutoOrderListByUser(request):
    user_id = request.user_id

    if not user_id:
        raise Exception("入参有误")

    order_list = order_handler.OrderHandler.queryAutoOrderListByUser(user_id)

    if order_list is None:
        raise Exception("查询列表为空")

    return order_list


def placeOrder(request):
    params = request.body.get("data")
    if not params or "order_address" not in params or "order_tag" not in params or "order_price" not in params:
        raise Exception("入参有误")
    order_user_id = request.user_id
    order_address = params["order_address"]
    order_tag = params["order_tag"]
    order_price = params["order_price"]

    data = order_handler.OrderHandler.placeOrderHandler(order_user_id, order_address, order_tag, order_price)

    if data is None:
        raise Exception("创建失败")
    elif data == -1:
        # 余额不足，请充值
        return -1

    return str(data)


def addChange(request):
    # params = request.body
    params = request.body.get("data")
    user_id = request.user_id
    add_change = params["add_change"]

    if not params:
        raise Exception("入参有误")
    data = order_handler.OrderHandler.addChangeHandler(user_id, add_change)
    return data


def minusChange(request):
    # params = request.body
    params = request.body.get("data")
    user_id = request.user_id
    minus_change = params["minus_change"]
    if not params:
        raise Exception("入参有误")

    data = order_handler.OrderHandler.minusChangeHandler(user_id, minus_change)
    print(data)

    return data


def queryOrderByOrderId(request):
    # params = request.body
    params = request.body.get("data")
    order_id = params["order_id"]
    data = order_handler.OrderHandler.queryOrderByOrderIdHandler(order_id)
    return data


def createOrderRemark(request):
    params = request.body.get("data")
    order_id = params["order_id"]
    order_remark = params["order_remark"]
    data = order_handler.OrderHandler.createOrderRemarkHandler(order_id, order_remark)
    print(data)
    return data


def orderPackage(request):
    # params = request.body
    params = request.body.get("data")
    order_user_id = request.user_id
    order_address = params["order_address"]
    order_tag = params["order_tag"]
    package_type = params["package_type"]
    if not params:
        raise Exception("入参有误")

    data = order_handler.OrderHandler.orderPackageHandler(order_user_id, order_address, order_tag, package_type)

    if data is None:
        raise Exception("购买失败")
    elif data == -1:
        # 余额不足
        return -1
    return str(data)


def packageQuery(request):
    order_user_id = request.user_id
    data = order_handler.OrderHandler.packageQueryHandler(order_user_id)
    return data
