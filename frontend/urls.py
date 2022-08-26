from django.urls import path
from frontend.views import home, aboutus


urlpatterns = [
    path('', home, name='home_front'),
    path('aboutus/', aboutus, name='aboutus'),
]

handler404 = 'frontend.views.handler404'