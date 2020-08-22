from django.urls import path
from .views import home,post_new,post_edit

urlpatterns = [
    path('',home,name='home'),
    path('post/new/',post_new,name='post_new'),
    path('post/<int:pk>/edit/',post_edit,name='post_edit'),

]