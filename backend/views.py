from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import NewsArticle, SubscribersEmail

def home(response):
    news = NewsArticle.objects.all()
    emails = SubscribersEmail.objects.all()
    context = {"news": news, "emails": emails}
    return render(response, 'backend/backend.html', context)

def newsList(response):
    news_sorted = NewsArticle.objects.order_by("-publishedAt")[:30]
    context = {"news": news_sorted}
    return render(response, 'backend/news_list.html', context)

def deleteNewsArticle(response, id):
    NewsArticle.objects.filter(id=id).delete()
    return redirect("news_list")

def editNewsArticle(response, id):
    if response.method == "POST":
        title = response.POST.get('title')
        urlToImage = response.POST.get('urlToImage')
        url = response.POST.get('url')
        description = response.POST.get('description')
        print(title)
        print(urlToImage)
        print(url)
        print(description)
        if title != None and len(title) > 90:
            title = title[:86]+" ..."
        if description != None and description.strip() != "" and len(description) > 250:
            description = description[:246]+" ..."
        news_article = NewsArticle.objects.get(id=id)
        news_article.title = title
        news_article.urlToImage = urlToImage
        news_article.url = url
        news_article.description = description
        news_article.save()
    news_article = NewsArticle.objects.get(id=id)
    context = {"news_article": news_article}
    return render(response, 'backend/edit_article.html', context)

