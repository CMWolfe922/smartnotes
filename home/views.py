from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView

# Creating the HomeView
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# Create authorized views here
# this is all I have to do to block access to a page if user isn't logged in.
# The login_url redirects the user to a page to login
@login_required(login_url="/admin")
def authorized(request):
    return render(request, "home/authorized.html", {})
