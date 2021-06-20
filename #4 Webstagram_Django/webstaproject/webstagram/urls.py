from django.urls import path
from .views import *

urlpatterns = [
    path('feed/', feed, name="feed"),
    path('detail/<str:id>', detail, name="detail"),
    path('profile/<str:id>', profile, name="profile"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]