from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),  # 在没有任何地址时，展示home
    path("user/", views.user, name="user")
]
