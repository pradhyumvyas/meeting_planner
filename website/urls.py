from django.urls import path
from . import views

urlpatterns = [
    path('website/index.html', views.welcome and views.date, name='index'),
]