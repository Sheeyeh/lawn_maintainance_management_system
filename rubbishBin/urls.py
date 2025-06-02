"""
URL configuration for Rubbish_bin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rubbishBin import order, clerk, user, device
from rubbishBin import test
from rubbishBin import login
from rubbishBin import repair

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("RB.url")),

    path("order/order/queryByUser", order.queryOrderListByUser),
    path("order/order/create", order.placeOrder),
    path("order/order/queryByOrder", order.queryOrderByOrderId),
    path("order/order/remark", order.createOrderRemark),
    path("order/package/create", order.orderPackage),
    path("order/package/query", order.packageQuery),
    path("order/device/queryByUser", order.queryAutoOrderListByUser),

    path("user/changes/query", order.changesQuery),
    path("user/changes/add", order.addChange),
    path("user/changes/fetch", order.minusChange),
    path("user/info/query", user.queryUserInfo),
    path("user/info/change", user.changeUserInfo),
    path("user/device/add", user.addDevice),

    path("clerk/clerk/qualify", clerk.qualifyClerk),
    path("clerk/clerk/qualification", clerk.clerkIsQualified),
    path("clerk/order/queryByStatus", clerk.queryOrderListByStatus),
    path("clerk/order/queryByClerk", clerk.queryOrderByClerkId),
    path("clerk/order/receive", clerk.receiveOrder),
    path("clerk/order/autoReceive", clerk.receiveAutoOrder),
    path("clerk/order/finish", clerk.clerkFinishOrder),
    path("clerk/order/finish", clerk.clerkFinishOrder),
    path("clerk/changes/query", clerk.clerkChangesQuery),
    path("clerk/changes/minus", clerk.clerkMinusChanges),
    path("clerk/changes/add", clerk.clerkAddChanges),
    path("clerk/info/change", clerk.changeClerkInfo),
    path("clerk/info/query", clerk.clerkInfoQuery),
    path("clerk/battery/change", clerk.clerkChangeBattery),
    path("clerk/battery/finish", clerk.clerkFinishBattery),

    path("device/height/fetch", device.fetchHeight),
    path("device/battery/fetch", device.autoBatteryHandler),

    path("repair/report", repair.repairReport),
    path("repair/query", repair.queryRepairList),
    path("repair/detail", repair.queryRepairDetail),
    path("repair/query/all", repair.queryRepairData),
    path("repair/change/status", repair.changeRepairStatus),

    path("test/get", test.test_get),
    path("test/post", test.test_post),
    path("wx/login", login.login),
    path("wx/clerkLogin", login.clerkLogin),
    path("wx/register", login.register),
    path("wx/clerkRegister", login.clerkRegister),
]
