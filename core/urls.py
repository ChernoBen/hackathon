from django.urls import path
from .views import home,post_new,post_edit,sou_mei

urlpatterns = [
    path('',home,name='home'),
    path('sou_mei',sou_mei,name='sou_mei'),
    path('post/new/',post_new,name='post_new'),
    path('post/<int:pk>/edit/',post_edit,name='post_edit'),

]