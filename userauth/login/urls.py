from django.urls import path
from login import views

app_name = 'Manish'

urlpatterns = [
    path('', views.home,name='home'),
    path('details/', views.detailsss, name='details'),
    path('registration/', views.register,name='registration')
]