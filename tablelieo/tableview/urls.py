
from django.urls import path
from . import views

urlpatterns = [
    path('table/',views.index),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    

]