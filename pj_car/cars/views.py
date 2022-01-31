from django.shortcuts import render

# Create your views here.
# /cars/

def show(request):
    return render(request, 'cars/html/show.html')

def add(request):
    return render(request, 'cars/html/add.html')

def delete(request):
    return render(request, 'cars/html/delete.html')
