from django.shortcuts import render

# Create your views here.
def rental_review(request):
    return render(request, 'cars/rental_review.html')

def thank_you(request):
    return render(request, 'cars/thank_you.html')
