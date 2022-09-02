from django.urls import path
from frontend.views import home, aboutus, keepAlive


urlpatterns = [
    path('', home, name='home_front'),
    path('aboutus/', aboutus, name='aboutus'),
    path('keepalive/', keepAlive, name='keepalive'),
]

handler404 = 'frontend.views.handler404'