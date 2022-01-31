from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('show/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]
