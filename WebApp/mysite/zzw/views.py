from django.shortcuts import render
import requests
import json


# Create your views here.
def home(request):
    # 请求数据
    api_request = requests.get("https://api.github.com/users?since=0")  # 使用GitHub提供的api接口
    api = json.loads(api_request.content)  # 取出接口中的建json
    return render(request, 'home.html', {"api": api})  # 展示home.html, home.html在templates目录下


def user(request):
    # 这里的'user' 对应于<input class="form-control mr-sm-2" name="user" type="search" placeholder="Search" aria-label="Search"> 中的name字段名
    if request.method == "POST":
        user = request.POST['user']
        api_request = requests.get("https://api.github.com/users/"+user)
        user_info = json.loads(api_request.content)
        return render(request, 'user.html', {'user_info': user_info})

    print("不是Post")
    not_found = "请在搜索框中输入您要查询的用户..."
    return render(request, 'user.html', {'not_found': not_found})
