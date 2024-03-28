from django.urls import path
from  .views import *
urlpatterns = [

    path('',dashboard,name="dashboard"),
    path('my-articles',user_articles,name="my-articles"),
    path('ajouter-article',addArticle.as_view(),name='ajouter-article')
]