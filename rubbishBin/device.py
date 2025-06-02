from handler import device_handler


def fetchHeight(request):
    device_list = device_handler.DeviceHandler.queryDeviceHandler()
    dev_id = device_list["devID"]
    data = device_handler.DeviceHandler.autoOrderByHeightHandler(dev_id)
    print(data)
    return data


def autoBatteryHandler(request):
    device_list = device_handler.DeviceHandler.queryDeviceHandler()
    dev_id = device_list["devID"]
    data = device_handler.DeviceHandler.autoBatteryHandler(dev_id)
    print(data)
    return data
