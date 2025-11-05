from django.shortcuts import render #to load page on browser
from django.shortcuts import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("Hello World!")

def custom(request):
    return HttpResponse("This is custom Response")