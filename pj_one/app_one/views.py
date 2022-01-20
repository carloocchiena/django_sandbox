from django.shortcuts import render
from django.http import HttpResponse

# /app_one/
def index(request):
    return HttpResponse("Hello, world. You're at the app_one index.")

def service_alfa(request):
    return HttpResponse("Hello, world. You're at the service_alfa.")

def service_beta(request):
    return HttpResponse("Hello, world. You're at the service_beta.")
    