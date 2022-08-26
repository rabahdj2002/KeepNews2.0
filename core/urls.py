# from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('admin/', include('backend.urls')),
]

handler404 = 'frontend.views.handler404'