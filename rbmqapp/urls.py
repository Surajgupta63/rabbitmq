from django.urls import path
from rbmqapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
