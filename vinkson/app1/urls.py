from django.urls import path
from app1 import views

app_name = 'vinkson'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('tech1/', views.tech1, name='tech1'),
    path('tech2/', views.tech2, name='tech2'),
    path('tech3/', views.tech3, name='tech3'),
    path('tech4/', views.tech4, name='tech4'),
    path('tech5/', views.tech5, name='tech5'),
    path('tech6/', views.tech6, name='tech6'),
]