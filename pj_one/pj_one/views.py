from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse("Hello, world. You're at the home page.")