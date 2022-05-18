from django.shortcuts import render

# import the Notes model from this app
from .models import Notes

def list_notes(request):
    # create an object that retrieves all the notes in the database
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
