from django.urls import path
from . import views

urlpatterns = [
    path('', views.activitate_list, name='activitate_list'),
]