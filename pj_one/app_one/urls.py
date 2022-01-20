from django.urls import path
from . import views

# /app_one/
urlpatterns = [
    path('', views.index, name='index'),
    path('service_alfa/', views.service_alfa, name='service_alfa'),
    path('service_beta/', views.service_beta, name='service_beta'),
]
