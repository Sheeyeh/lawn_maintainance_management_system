from django.http import JsonResponse
def buildSuccessResponse(data):
    wrappedResponseData = {
            'success': True,
            'data': data,
    }
    return JsonResponse(wrappedResponseData,safe=False)
def buildExceptionResponse(router,errMsg='编码错误',status_code=500):
    response = JsonResponse({
        'success':False,
        'error':{
            'errMsg':'接口{}报错,原因:{}'.format(router,errMsg)
        }
    }) 
    response.status_code = status_code
    return response