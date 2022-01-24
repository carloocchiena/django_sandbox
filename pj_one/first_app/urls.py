from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('<int:page_number>', views.page_num_view),
    path('variables/', views.variables_view),
    path('<str:topic>/', views.news_view, name='topic-page'),
]