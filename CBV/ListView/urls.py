from django.urls import path
from . import views

app_name = "Manish"

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('(?P<pk>[-\w]+)/', views.SchoolDetailView.as_view(), name='detail')
]
