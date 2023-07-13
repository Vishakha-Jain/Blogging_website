from .views import *
from django.urls import path,include
urlpatterns = [

    path("",home),
    # slug means dynamic url
    path("blog/<slug:url>",post),
    path("category/<slug:url>",category),

]