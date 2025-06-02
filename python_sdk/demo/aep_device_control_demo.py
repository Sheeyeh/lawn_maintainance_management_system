#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_control

if __name__ == '__main__':
    result = apis.aep_device_control.QueryRemoteControlList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_device_control.CreateRemoteControl('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

