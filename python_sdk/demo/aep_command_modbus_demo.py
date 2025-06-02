#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_command_modbus

if __name__ == '__main__':
    result = apis.aep_command_modbus.QueryCommandList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '10015488', '10015488test')
    print('result='+str(result))

    result = apis.aep_command_modbus.QueryCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488, '10015488test')
    print('result='+str(result))

    result = apis.aep_command_modbus.CancelCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_command_modbus.CreateCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

