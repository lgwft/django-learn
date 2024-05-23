from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def movie_list(request):
    return HttpResponse("电影app页面")

def movie_detail(request,movie_id):
    return HttpResponse(f"你正在查询的电影id是：{movie_id}")