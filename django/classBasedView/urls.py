from django.conf.urls import url
from django.urls import path
from classBasedView import views
from django.conf import settings


app_name = "classBasedView"

urlpatterns = [
    path('', views.ClassBasedView.as_view(), name='classBasedView'),
    path('detail/<pk>/', views.ClassDetailView.as_view(), name='classDetail'),
    path('add_musician/', views.AddMusician.as_view(), name='addMusician'),
    path('update_musican/<pk>/', views.AddMusician.as_view(), name='updateMusician'),
    path('delete_musican/<pk>/', views.DeleteMusician.as_view(), name='deleteMusician'),
]