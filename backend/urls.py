from django.urls import path
from django.shortcuts import redirect
from backend.views import home, newsList, deleteNewsArticle, editNewsArticle, emailsList, deleteEmailsArticle


urlpatterns = [
    path('', lambda request: redirect('dashboard/', permanent=False)),
    path('dashboard/', home, name='home'),
    path('news/', newsList, name='news_list'),
    path('news/delete/<int:id>/', deleteNewsArticle, name='delete_news_article'),
    path('news/edit/<int:id>/', editNewsArticle, name='edit_news_article'),
    path('emails/', emailsList, name='emails_list'),
    path('emails/delete/<int:id>/', deleteEmailsArticle, name='delete_news_article'),
]
