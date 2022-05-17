# CREATING A SMART NOTES DJANGO PROJECT:
---

> This is a tutorial project to help better understand the django development process.

---

### CREATE SECOND APP:
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

## THE home002 BRANCH:

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
