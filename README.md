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
