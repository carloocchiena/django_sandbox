from django.http import HttpResponse
from django.shortcuts import render


# probably would make sense to link this to a template within an home_page_app
def index_view(request):
    return render(request, 'base_template.html')