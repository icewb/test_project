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
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
           #return HttpResponse("用户名或密码不能为空")
           return render(request,"index.html",{"error":"用户名或密码不能为空啊"})
        
        if username == "admin" and password == "123456":
            return render(request,"project_manager.html",{"messange":"欢迎进入管理页面"})


