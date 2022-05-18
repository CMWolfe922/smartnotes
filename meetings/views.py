from django.shortcuts import render

from .models import Meeting

def meetings_list(request):
    meeting = Meeting.objects.all()
    return render(request, 'meetings.html', {'meetings': meeting})
    