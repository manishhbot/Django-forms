from django.urls import path
from my_first_1 import views

urlpatterns=[
    path('', views.help, name='anything')
]
