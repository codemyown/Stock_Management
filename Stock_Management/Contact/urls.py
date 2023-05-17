from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("register/",views.Registration),
    path("login/",views.login),
    path("order/",views.order),
    path("",views.index)
]
