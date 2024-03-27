from django.urls import path
from  .views import *
urlpatterns = [

    path('',dashboard,name="dashboard"),
    path('my-articles',user_articles,name="my-articles"),
]