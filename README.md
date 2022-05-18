# CREATING A SMART NOTES DJANGO PROJECT:
---

> This is a tutorial project to help better understand the django development process.

---

## CREATE SECOND APP:
> For the second app, I am going to create a home app

- This will be our apps "home" page/features

---
> I created a function home in the home directories `views.py` file that will return "Hello, world!" anytime it receives a request for the home url.

- now to register this, go to the main urls.py file in my smartnotes directory and import:

    `from home import views`

- Then add a new path:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    # add new path
    path('home', views.home),
]
```

---
# THE MVT FRAMEWORK:
### _The Model, View, Template Framework_

- The `MODEL` is what creates, manages and deploys databases and database tables, features and their configurations.

- The `VIEW` is the functions and methods that control the Template part of this whole framework.

- The `TEMPLATE` is the html files that get presented to users as the frontend. But they also need to accept user input and handle logical functionality

---

### THE home002 BRANCH:

- update the `views.py` file. I need to change the base function instead of `HttpResponse` I will use `render`.

This uses 3 parameters, __original request__, __name of template__ and __empty brackets__

```python
def views_func_using_render(request):

    # uses 3 parameters
    return render(request, "home/welcome.html", {})
```

- You leave the brackets empty since I am using a template framework to create the final html page.

- use brackets to pass down information from the view, to the template:
    - By doing this I can modify my template to receive a varaiable containing whatever data is inside the brackets

- EXAMPLE: Adding time and date
```python
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def home(request):
    # This is saying whenever it gets a home request return hello world
    return render(request, "Hello, world!", {'today': datetime.today()})
```

---
### BRANCH home003:

- Updated the `views.py`, `home/urls.py`, and added a new template in the `templates` directory. `authorized.html` which contains a view that only allows logged in users to access.

- In order to restrict people from seeing a page if they are not logged in, you must use the `from django.contrib.auth.decorators import login_required` package to then decorate whichever view you want restricted.

    - Example:
    ```python
    from django.contrib.auth.decorators import login_required

    # Create authorized views here
    # this is all I have to do to block access to a page if user isn't logged in.
    @login_required
    def authorized(request):
        return render(request, "home/authorized.html", {})
    ```

- You can also add a redirect url so the user doesn't get a 404 message:

    - Example:
    ```python
    from django.contrib.auth.decorators import login_required

    # Create authorized views here
    # this is all I have to do to block access to a page if user isn't logged in.
    # The login_url redirects the user to a page to login
    @login_required(login_url="/admin")
    def authorized(request):
        return render(request, "home/authorized.html", {})
    ```

> The `login_url` which redirects users should be used to redirect them to a page that will allow them to login. OR maybe give an option to login or register.

---

## CREATE A NEW APP NOTES:
> `django-admin startapp notes`

> This app will be used to practice building models and using the django ORM.
---

### BRANCH notes001:

- In this branch I created the actual notes app and built the Notes class in models.

    - Example:
    ```python
    from django.db import models

    # Create your models here.
    class Notes(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
    ```

- Now I have to create migrations:
`python manage.py makemigrations`

- Once this is done, I will then need to migrate the changes:
`python3 manage.py migrate`

---

### BRANCH notes002:

- In this branch I setup the Django admin interface to include the Notes model.

> To add the Notes model to the admin interface, I have to add these lines of code to the `admin.py` file in `notes` app

```python
from django.contrib import admin

from . import models
# Register your models here. This is where you decide which models can
# be displayed in the admin interface

class NotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Notes, NotesAdmin)
```

> Now check the admin page in the browser and the notes model will be there and will allow me to add or remove notes.
---

### BRANCH notes003:

- In this branch I will update how the notes show up in the database and in the admin interface. Right now a new note shows up as Notes object(1)

> To change this go to the `notes/admin.py` file and go to the `NotesAdmin` class and update this class to have:

```python
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', )
```
---

# USING DJANGO'S SHELL:

> We can use Django's shell to practice querying models, creating new models and filtering those querysets.

- Below is examples of how to use the Django shell

```sh
(djangoenv) blackbox@BlockBox:~/projects/web-projects/django_projects/smartnotes$ python3 manage.py shell
/home/blackbox/.local/lib/python3.8/site-packages/IPython/core/interactiveshell.py:841: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
  warn(
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from notes.models import Notes

In [2]: mynote = Notes.objects.get(pk='1')

In [3]: mynote.title
Out[3]: 'My First Note'

In [4]: mynote.text
Out[4]: 'Adding my first note to the Django smartnotes project! I added this note using the admin interface.'

In [5]: Notes.objects.all()
Out[5]: <QuerySet [<Notes: Notes object (1)>]>

In [6]: new_note_text = "This is a second note created in the django shell"

In [7]: new_note_title = "Second Note: Created in Shell"

In [8]: new_note = Notes.objects.create(title=new_note_title, text=new_note_text)

In [9]: Notes.objects.all()
Out[9]: <QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>]>

In [10]: Notes.objects.filter(title__startswith="Second")
Out[10]: <QuerySet [<Notes: Notes object (2)>]>

In [11]: Notes.objects.filter(text__icontains="note")
Out[11]: <QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>]>

In [12]: Notes.objects.filter(text__icontains="second")
Out[12]: <QuerySet [<Notes: Notes object (2)>]>

In [13]: Notes.objects.filter(text__icontains="first")
Out[13]: <QuerySet [<Notes: Notes object (1)>]>

In [14]: Notes.objects.exclude(text__icontains="first")
Out[14]: <QuerySet [<Notes: Notes object (2)>]>

In [15]: Notes.objects.filter(text__icontains="first").exclude(title__icontains="Second")
Out[15]: <QuerySet [<Notes: Notes object (1)>]>
```
---

### BRANCH dynamic-template:

> this branch will be used to create a template that loads data dynamically using the models I have created. To do this I will have to create new views in the `notes/views.py` file and then create `templates` in the `notes/templates/notes` directory:

- In the `views.py` file add this function:
```python
from django.shortcuts import render

# import the Notes model from this app
from .models import Notes

def list_notes(request):
    # create an object that retrieves all the notes in the database
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
```

> Next create a new `urls.py` file in the notes app and add this code:

```python
from django.urls import path

from . import views

urlpatterns =[
    path('notes', views.list_notes)
]
```

> next I will have to add this urlpattern to the smartnotes main `urls.py` file

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),

    # LINE THAT NEEDS TO BE ADDED:
    # This path is for the list_notes view in the notes app
    path('smart/', include('notes.urls')),
]
```
> Now that the backend logic is setup, I need to build the template html file to render the notes. This is a very simple template:

```html
<html>
<h1>These are all the notes: </h1>

<ul>
    {% for note in notes %}
    <li>{{note.title}}</li>
    {% endfor %}
</ul>

</html>
```

- This template can be accessed at `smart/notes` in the url.
