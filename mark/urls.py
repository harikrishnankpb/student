
from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('addmark',views.addmark,name="addmark"),
    path('viewmark',views.viewmark,name="viewmark")
]