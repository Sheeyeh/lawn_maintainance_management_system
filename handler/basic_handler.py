from datetime import date, datetime
import json
import time


# 基础处理器

class ComplexEncoder(json.JSONEncoder):
    # json编码格式
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        else:
            return json.JSONEncoder.default(self, obj)


class TimeHandler:
    # 时间格式转换
    @staticmethod
    def timestampHandler(timestamp=None):
        # 获取当前时间戳，并返回DatetimeField结果(str)
        if not timestamp:
            timestamp = int(datetime.now().timestamp())
        timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        return str(timestr)
