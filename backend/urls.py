from django.urls import path, include
from backend.views import *


urlpatterns = [
    path('', home, name='home'),
]
