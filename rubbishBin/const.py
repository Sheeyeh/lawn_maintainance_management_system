from rubbishBin.utils import const


# 配置项：配置路由到路由方法和是否需要请求体的映射
# bodyRequired默认为False,method默认为POST
class configItem:
    def __init__(self, item) -> None:
        self.configItem = item

    def __getitem__(self, key):
        if key == 'method':
            if not self.configItem.get(key, None):
                return 'POST'
            else:
                return self.configItem[key]
        if key == 'bodyRequired' and not self.configItem.get(key, None):
            if not self.configItem.get(key, None):
                return True
            else:
                return self.configItem[key]


class controllerValidate:
    def __init__(self, config) -> None:
        self.config = {}
        for router in config:
            self.config[router] = configItem(config[router])

    def __getitem__(self, key):
        return self.config.get(key, {
            'method': 'POST',
            'bodyRequired': True
        })


# 在这里配置
config = {
    '/order/changes/query': {
        'method': 'POST',
        'bodyRequired': True
    },
    '/order/queryOrderList': {
        'method': 'POST',
        'bodyRequired': False
    },
    '/test/get': {
        'method': 'GET'
    },
    '/test/post': {
        'method': 'POST'
    }
}
const.controllerValidate = controllerValidate(config)
