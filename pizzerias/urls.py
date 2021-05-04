# path function needed when mapping URLs to views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# the dot tells Python to import the views.py module from
# the same directory as the current urls.py module
from . import views

# the variable app_name helps Django distinguish
# this urls.py file from files of the same name in other apps within the project
app_name = "pizzerias"

# the variable urlpatterns in this module is a list of individual pages that
# can be requested form the pizzerias app
urlpatterns = [
    # the first argument is an empty string ('') which matches the base URL
    # http://localhost:8000/. the second argument specifies the function name to
    # call in views.py the third argument provides the name 'index' for the URL
    # pattern to refer to it later
    path("", views.index, name="index"),
    path("name", views.names, name="names"),
    # integer value is stored in the variable name_id and will be
    # subsequently passed to the topic funtion in views.py
    path("names/<int:name_id>/", views.name, name="name"),
    path("new_name/", views.new_name, name="new_name"),
    path("new_comment/<int:name_id>/", views.new_comment, name="new_comment"),
]

urlpatterns += staticfiles_urlpatterns()
