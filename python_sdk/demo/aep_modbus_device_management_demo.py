#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_modbus_device_management

if __name__ == '__main__':
    result = apis.aep_modbus_device_management.UpdateDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '10015488test', '{}')
    print('result='+str(result))

    result = apis.aep_modbus_device_management.CreateDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_modbus_device_management.QueryDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '10015488test', 10015488)
    print('result='+str(result))

    result = apis.aep_modbus_device_management.QueryDeviceList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_modbus_device_management.DeleteDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_modbus_device_management.ListDeviceInfo('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

