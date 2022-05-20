from django.shortcuts import render
from django import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

class LoginView(View):
    
    @login_required(login_url='/admin')
    def login(self, request, *args, **kwargs):
        return render(request, 'admin.html')