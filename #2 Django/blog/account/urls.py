from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', register_view, name="signup"),
]