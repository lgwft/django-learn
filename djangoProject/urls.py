"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.shortcuts import HttpResponse
from django.urls import path,include,reverse
from book import views


def index(request):
    return HttpResponse("欢迎你，lgw")

# path函数详解
# path(router,view,name=None,Kwargs=None）
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("book", views.book_detail_query_string),
    # router参数 传递参数通过<>尖括号来进行指定，并且传递参数的时候可以指定这个参数的数据类型
    # str int slug:由英文中的- _连接英文字符或者数字而成的字符串 uuid path:匹配非空的英文字符串，可以包含/
    path("book/<int:book_id>", views.book_detail_path),
    # 在项目主文件urls下包含多个app的路径映射略显凌乱，可以通过路由模块化解决
    path("movie/", include("movie.urls"))
]
