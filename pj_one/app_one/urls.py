from django.urls import path
from . import views

# /app_one/
urlpatterns = [
    path('', views.index),
    path('<int:service_num>', views.redirect_service),
    path('<str:service_name>/', views.service_view, name='service_view'),
]
