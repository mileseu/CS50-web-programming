from django.urls import path

#import variable name from current dir
from . import views

#list of all allowable urls that can be accessed for this app
urlpatterns = [
    #empty string - no additional arguments, what view should be rendered when this path is visited
    path("", views.index, name="index"),
    path("miles", views.miles, name="miles"),
    path("<str:name>", views.greet, name="greet")
]