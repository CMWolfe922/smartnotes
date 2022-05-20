from django.shortcuts import render
from django.http import Http404
# import the Notes model from this app
from .models import Notes
from django.views.generic import ListView, DetailView

# Create a ListView 
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # I can also add a template name here if I want to specify the name:
    template_name = "notes/notes_list.html"

class NoteDetailsView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/note_details.html"
