from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def home(request):
    # This is saying whenever it gets a home request return hello world
    return render(request, "home/welcome.html", {'today': datetime.today()})

# Create authorized views here
# this is all I have to do to block access to a page if user isn't logged in.
# The login_url redirects the user to a page to login
@login_required(login_url="/admin")
def authorized(request):
    return render(request, "home/authorized.html", {})
