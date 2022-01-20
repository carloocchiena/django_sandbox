from django.urls import path
from . import views

# /app_one/
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:service_name>/', views.service_view, name='service_view')
]
