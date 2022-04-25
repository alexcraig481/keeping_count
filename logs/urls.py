"""Defines URL patterns for the logs"""

from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('dates/', views.logs, name="logs")
]
