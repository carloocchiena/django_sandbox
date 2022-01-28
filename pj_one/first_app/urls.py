from django.urls import path
from . import views

# assign the app namespace
app_name = 'first_app'

urlpatterns = [
    path('', views.main_view, name='app_home'),
    path('variables/', views.variables_view, name='variables'),
    path('get_all/', views.get_all, name='get_all'),
    path('<int:page_number>', views.page_num_view, name='redirect'),
    path('<str:topic>/', views.news_view, name='topic-page'),
]