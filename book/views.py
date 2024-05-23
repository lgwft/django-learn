from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 在url中携带参数
# 1.通过查询字符串携带参数：http://localhost:8080/search?wd=python&a=1&b=2
# 2.通过路径参数：http://localhost:8080/book/2

# 1.通过查询字符串携带参数：http://localhost:8080/book?id=3
def book_detail_query_string(request):
    id = request.GET.get('id')
    return HttpResponse(f"你正在查找的书籍编号是：{id}")


# 2.通过路径参数：http://localhost:8080/book/2
def book_detail_path(request,book_id):
    return HttpResponse(f"你正在查找的书籍编号是：{book_id}")
