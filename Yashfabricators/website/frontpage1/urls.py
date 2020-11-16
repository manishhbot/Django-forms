from django.urls import path
from frontpage1 import views

app_name = 'Aman'

urlpatterns = [
    path('one/', views.home, name='home'),
    path('contact/', views.contact_d, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutpage, name='logout')
]