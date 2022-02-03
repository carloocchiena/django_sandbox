from django.urls import path
from . import views

app_name = 'classroom'

# /classroom/
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    ]