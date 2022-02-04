from django.urls import path
from . import views

app_name = 'classroom'

# /classroom/
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('teacher_create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    ]
