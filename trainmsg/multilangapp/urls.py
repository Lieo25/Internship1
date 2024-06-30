from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    
    path('insert/',views.insert,name='insert'),

    path('translate/',views.translate_tamil,name='translate'),

    

]