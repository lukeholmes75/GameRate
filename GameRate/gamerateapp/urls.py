from django.urls import path
from gamerateapp import views

app_name = 'gamerateapp'

urlpatterns = [
	path('', views.index, name='index'),
]
