from django.urls import include, re_path, path
from . import views


urlpatterns = [

    path('', views.homepage, name=""),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),

]