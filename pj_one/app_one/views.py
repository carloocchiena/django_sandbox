from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# /app_one/

# available services

services = {
    'service_alfa': 'the first service',
    'service_beta': 'the second service',
    'service_gamma': 'the third service'
}

# functions views

def index(request):
    return HttpResponse("Hello, world. You're at the app_one index.")

def service_view(request, service_name):
    try: 
        service_name = services[service_name]
        return HttpResponse(f"Hello, world. You're at the {service_name} section.")
    except:
        raise Http404("<h1>404 - Page not found</h1>")


# redirect function

def redirect(request, service_num):
    service_list = list(services.keys())
    service = service_list[service_num]
    webpage = reverse('service_view', args=[service])
                           
    return HttpResponseRedirect(webpage)
