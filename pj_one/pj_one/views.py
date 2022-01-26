from django.http import HttpResponse


# probably would make sense to link this to a template within an home_page_app
def index_view(request):
    return HttpResponse("<h1>Hello World!<h1>")