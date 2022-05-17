from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def home(request):
    # This is saying whenever it gets a home request return hello world
    return render(request, "home/welcome.html", {'today': datetime.today()})
