from django.urls import path
from .views import *

urlpatterns = [
    path('',ResgisterUserView.as_view())
]