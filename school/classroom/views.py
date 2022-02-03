from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

from . import forms
from . import models

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'
    
class TeacherCreateView(CreateView):
    model = models.Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')
       
class ContactFormView(FormView):
    form_class = forms.ContactForm
    template_name = 'classroom/contact.html'
    
    # what to do if the form is submitted and valid
    success_url = reverse_lazy('classroom:thank_you')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        
    