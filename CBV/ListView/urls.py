from django.urls import path
from django.conf.urls import  url
from . import views

app_name = "Manish"

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
    # path('(?P<pk>[-\w]+)/', views.SchoolDetailView.as_view(), name='detail')
]
