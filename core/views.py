from django.http.request import HttpRequest
from core.models import Contact
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    return render(request, 'core/home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

    return render(request, 'contact.html')    
    #return render(request, 'core/home.html')

    


    