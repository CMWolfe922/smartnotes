from django.shortcuts import render

# import the Notes model from this app
from .models import Notes

def list_notes(request):
    # create an object that retrieves all the notes in the database
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


# Create a view that displays note details
def note_details(request, pk):
    # get the note using the primary key
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/note_details.html', {'note': note})
