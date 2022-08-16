from django.shortcuts import render, redirect
from datetime import datetime
from frontend.models import NewsArticle, SubscribersEmail


def home(response):
    news = NewsArticle.objects.all()
    emails = SubscribersEmail.objects.all()
    context = {"news": news, "emails": emails}
    return render(response, 'backend/home.html', context)


def newsList(response):
    news_sorted = NewsArticle.objects.order_by("-publishedAt")[:30]
    if response.method == "POST":
        search = response.POST.get('search')
        try:
            news_sorted = [NewsArticle.objects.get(id=search)]
        except Exception:
            try:
                news_sorted = NewsArticle.objects.filter(title__contains=search)
            except Exception:
                context = {"news": []}
                return render(response, 'backend/news_list.html', context)
    context = {"news": news_sorted}
    return render(response, 'backend/news_list.html', context)


def deleteNewsArticle(response, id):
    NewsArticle.objects.filter(id=id).delete()
    return redirect("news_list")


def editNewsArticle(response, id):
    try:
        NewsArticle.objects.get(id=id)
    except Exception:
        return redirect('news_list')
    if response.method == "POST":
        title = response.POST.get('title')
        urlToImage = response.POST.get('urlToImage')
        url = response.POST.get('url')
        description = response.POST.get('description')
        try:
            publishedAt = datetime.strptime(response.POST.get('date'), "%b. %d, %Y").strftime('%Y-%m-%d')
        except Exception:
            return redirect('edit_news_article', id)
        if title is not None and len(title) > 90:
            title = title[:86]+" ..."
        if description is not None and description.strip() != "" and len(description) > 250:
            description = description[:246]+" ..."
        news_article = NewsArticle.objects.get(id=id)
        news_article.title = title
        news_article.urlToImage = urlToImage
        news_article.url = url
        news_article.description = description
        news_article.publishedAt = publishedAt
        news_article.save()
    news_article = NewsArticle.objects.get(id=id)
    context = {"news_article": news_article}
    return render(response, 'backend/edit_article.html', context)
