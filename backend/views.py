from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from frontend.models import NewsArticle, SubscribersEmail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import requests

@login_required
def home(response):
    if response.method == 'POST':
        return HttpResponse('Site Is Running')
    news = NewsArticle.objects.all()
    emails = SubscribersEmail.objects.all()
    context = {"news": news, "emails": emails}
    return render(response, 'backend/home.html', context)

@login_required
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

@login_required
def deleteNewsArticle(response, id):
    NewsArticle.objects.filter(id=id).delete()
    return redirect("news_list")

@login_required
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

@login_required
def emailsList(response):
    emails = SubscribersEmail.objects.all()[:30]
    if response.method == "POST":
        search = response.POST.get('search')
        try:
            emails = [SubscribersEmail.objects.get(id=search)]
        except Exception:
            try:
                emails = SubscribersEmail.objects.filter(email__contains=search)
            except Exception:
                context = {"emails": []}
                return render(response, 'backend/emails_list.html', context)
    context = {"emails": emails}
    return render(response, 'backend/emails_list.html', context)

@login_required
def deleteEmails(response, id):
    SubscribersEmail.objects.filter(id=id).delete()
    return redirect("emails_list")

@login_required
def sendEmails(response, id):
    pass


def userLogout(response):
    logout(response)
    return redirect('user_login')


def userLogin(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)            
            return redirect('home')
        else:
            return redirect('user_login')
    return render(response, 'backend/login.html', {})


def userForgotPwd(response):
    main_url = f"{ response.scheme }://{ response.META['HTTP_HOST'] }/"
    print(main_url)
    if response.method == 'POST':
        email = response.POST['email']
        try:
            user = User.objects.get(email=email)
            url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
            payload = {
                "personalizations": [
                    {
                        "to": [{"email": email}],
                        "subject": "Password Reminder!"
                    }
                ],
                "from": {"email": "team@keepnews.com"},
                "content": [
                    {
                        "type": "text/plain",
                        "value": f"Your Password is: {main_url}admin/reset_password/{str(user.password)[:50]}/"
                    }
                ]
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "22606cdc51mshb55e1156ae0b717p1f67c2jsn0b17cef6e7c0",
                "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            print(response.text)
            return redirect('user_login')
        except Exception as e:
            print(e)
            messages.warning(response, 'Account Does Not Exist!!')
            return redirect('user_forgot_pwd')
    return render(response, 'backend/forgot_pwd.html', {})


def resetPassword(response, hash):
    if response.method == 'POST':
        password = response.POST['password']
        user = User.objects.get(username='rabahdjebbes')
        user.set_password(password)
        user.save()
        return redirect('user_login')
    user = User.objects.get(username='rabahdjebbes')
    if str(user.password)[:50] == hash:
        return render(response, 'backend/reset_password.html', {})
    else:
        return redirect('user_forgot_pwd')
