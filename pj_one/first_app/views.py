from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from . import models

# /first_app/

# sections

articles = {
    "sports":"Welcome to the sports page",
    "finance":"Finance news here",
    "politics":"Politics is in the news"
}

# function views

# /
def main_view(request):
    return render(request,'first_app/home_app.html')

# /get_all
def get_all(request):
    
    all_users = models.MyModel.objects.all()
    context = {'users':all_users}
    
    return render(request, 'first_app/get_all.html', context=context)

# /variables/
def variables_view(request):
    
    my_var = {'first_name':'John','last_name':'Doe', 'a_list':["dog","cat","mouse"], 'a_dict':{'a':1,'b':2,'c':3}, 'user_auth':True}
    
    return render(request,'first_app/variables.html', context=my_var)

# redirects

def news_view(request,topic):
    try:
        headline = f"<h1>{articles[topic]}</h1>"
        return HttpResponse(headline)
    except:
        headline = "<h1>No article page for that topic!</h1>"
        return HttpResponseNotFound(headline)

pages = ['sports','finance','politics']

def page_num_view(request,page_number):
    topic = pages[page_number]
    return HttpResponseRedirect(topic)

def num_page_view(request,num_page):

    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    
    return HttpResponseRedirect(reverse('topic-page',args=[topic]))
