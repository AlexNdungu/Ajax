from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('getProfiles', views.getProfiles, name='getProfiles'),
    path('form/', views.Form, name='form'),
    path('create/', views.Create, name='create'),

    path('main/', views.AjaxForm, name='AjaxForm'),
]