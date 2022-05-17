from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # This is saying whenever it gets a home request return hello world
    return HttpResponse("Hello, world!")
