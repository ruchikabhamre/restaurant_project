from django.urls import path
from . import views
urlpatterns = [
    path("/booktable", views.contact,name="contact"),
    path("", views.index,name="home"),
   

]