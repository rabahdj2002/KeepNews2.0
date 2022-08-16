from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import NewsArticle, SubscribersEmail

def home(response):
    return render(response, 'backend/backend.html', {})

