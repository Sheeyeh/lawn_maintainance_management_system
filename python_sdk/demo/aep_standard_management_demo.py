#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_standard_management

if __name__ == '__main__':
    result = apis.aep_standard_management.QueryStandardModel('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

