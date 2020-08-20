from django.contrib import admin
from django.urls import path
from iReads import views

urlpatterns = [
    path('', views.index,name='home' ),
    path('stories', views.stories,name='stories' ),
    path('discussion', views.discussion,name='discussion' ),
    path('threadlist', views.threadlist,name='threadlist' ),
    path('thread', views.thread,name='thread' ),
    path('submitPost', views.submitPost,name='submitPost' ),
    path('submitComment', views.submitComment,name='submitComment' ),
    path('loginUser', views.loginUser,name='loginUser' ),
    path('signupUser', views.signupUser,name='signupUser' ),
    path('logoutUser', views.logoutUser,name='logoutUser' ),
]