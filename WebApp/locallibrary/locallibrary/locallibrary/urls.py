"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 这个新项目包括一个 path() ，
# 它将带有 catalog/ 的请求转发到模块 catalog.urls (使用相对路径 URL /catalog/urls.py)
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

"""
现在让我们把网站的根URL(例：127.0.0.1:8000)重定向到该URL：127.0.0.1:8000/catalog/; 
这是我们将在这个项目中使用的唯一应用程序，所以我们最好这样做。为了完成这个目标，
我们将使用一个特殊的视图函数(RedirectView), 当在 path() 函数中指定的URL模式匹配时（
在这个例子中是根URL），它将新的相对URL作为其第一个参数重定向到（/catalog/）。
"""
urlpatterns += [
    # 当没有指定path时会默认定位到http://127.0.0.1:8000/catalog/中，
    # 因为catalog目前是我们唯一的应用
    path('', RedirectView.as_view(url='/catalog/')),
]
"""
将路径函数的第一个参数留空以表示'/'。如果你将第一个参数写为'/'，
Django会在你启动服务器时给出以下警告：
System check identified some issues:

WARNINGS:
?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'. 
Remove this slash as it is unnecessary. 
If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
"""

"""
Django 默认不提供CSS, JavaScript, 和图片等静态文件 。
但是当你在开发环境中开发时，这些静态文件也很有用。作为对这个URL映射器的最后一项添加，
你可以通过添加以下行在开发期间启用静态文件的服务。
把下面的代码加到文件最后：
"""
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
