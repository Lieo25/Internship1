from django.contrib import admin  
from django.urls import path       
from .views import * 
from django.conf import settings   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
 
# Define URL patterns
urlpatterns = [
    path('home/', home, name="recipes"),     
    path('login/', login_user, name='login_page'),   
    path('register/', register, name='register'),
]