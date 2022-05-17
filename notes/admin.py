from django.contrib import admin

from . import models
# Register your models here. This is where you decide which models can
# be displayed in the admin interface

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(models.Notes, NotesAdmin)
