#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_subscribe_north

if __name__ == '__main__':
    result = apis.aep_subscribe_north.GetSubscription('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_subscribe_north.GetSubscriptionsList('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_subscribe_north.DeleteSubscription('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488test', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_subscribe_north.CreateSubscription('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

