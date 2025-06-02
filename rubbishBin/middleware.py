from typing import Any
from django.http import HttpResponse
import json
from ResponseFactory.factory import buildExceptionResponse, buildSuccessResponse

from rubbishBin.utils.jwt import parse_payload


class HandleHttpMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def handle_request_body(self):
        if self.method == 'GET':
            return self.queryDict
        return json.loads(self.request_body) if self.contentType == 'application/json' else self.request_body

    def __call__(self, request):
        self.request_body = request.body
        self.queryDict = {key: dict(request.GET)[key][0] for key in dict(request.GET)}
        self.method = request.method
        self.contentType = request.META['CONTENT_TYPE']
        print(self.contentType)
        return self.handleHttp(request)

    def handleHttp(self, request):
        request._body = self.handle_request_body()
        response = self.get_response(request)
        if isinstance(response, HttpResponse):
            if response.status_code != 200:
                return response
        else:
            return buildSuccessResponse(response)


class ErrorHandlerMiddleWare:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        return self.get_response(request)

    def process_exception(self, request, exception):
        return buildExceptionResponse(request.path_info, str(exception))


class JwtAuthorizationMiddleware:
    """
    用户需要通过请求头的方式来进行传输token，例如：
    Authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzM1NTU1NzksInVzZXJuYW1lIjoid3VwZWlxaSIsInVzZXJfaWQiOjF9.xj-7qSts6Yg5Ui55-aUOHJS4KSaeLq5weXMui2IIEJU
    """

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        return self.process_request(request)

    def process_request(self, request):

        # 如果是登录/注册，则通过
        if request.path_info == '/wx/login' or request.path_info == '/wx/clerkLogin' or request.path_info == '/repair/query/all' or request.path_info == '/repair/change/status':
            return self.get_response(request)

        # 非登录页面需要校验token
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        auth = authorization.split()
        # 验证头信息的token信息是否合法
        if not auth:
            return buildSuccessResponse({'loginStatus': False, 'msg': 'Your token is wrong, please login again!'})
        elif len(auth) > 1:
            return buildSuccessResponse({'loginStatus': False, 'msg': 'Your token is wrong, please login again!'})

        token = auth[0]
        # 解密
        result = parse_payload(token)
        if not result['status']:
            return buildSuccessResponse({'loginStatus': False, 'msg': result['error']})
        # 将解密后数据赋值给user_id
        request.user_id = result['data']['user_id']
        return self.get_response(request)
