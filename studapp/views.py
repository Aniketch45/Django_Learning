from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("Hello World!")

def custom(request):
    return HttpResponse("hello custom")