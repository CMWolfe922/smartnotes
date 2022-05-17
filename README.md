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
