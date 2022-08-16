from django.urls import path, include
from backend.views import *


urlpatterns = [
    path('', lambda request: redirect('dashboard/', permanent=False)),
    path('dashboard/', home, name='home'),
    path('news/', newsList, name='news_list'),
    path('news/delete/<int:id>/', deleteNewsArticle, name='delete_news_article'),
    path('news/edit/<int:id>/', editNewsArticle, name='edit_news_article'),
]
