from django.contrib import admin
from django.urls import path
from .views import create_post, homepage, posts, show_post


urlpatterns = [
    path('', homepage,name='homepage'),
    path('posts/',posts,name='posts'),
    path('create_post',create_post,name='createpost'),
    path('<int:id>/',show_post,name='show_post'),

]