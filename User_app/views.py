from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 首页
def index(request):
    #return render(request,"index.html")
    # print(request.method)
    # print(request.path)
#  return   HttpResponse(content="""
# """)
     return render(request,"index.html")

#处理登陆请求
def login_action(request):
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")

        if username == "" or password == "":
           #return HttpResponse("用户名或密码不能为空")
           return render(request,"index.html",{"error":"用户名或密码不能为空啊"})


