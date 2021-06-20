from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('blog/new',new,name="new"),
    path('blog/create',create,name="create"),
    path('blog/<int:blog_id>', detail, name="detail"),
    path('profile/<int:author_id>', profile, name="profile"),
]
