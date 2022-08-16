from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsArticle, SubscribersEmail

def home(response):
    if response.method == 'POST':
        mail = response.POST.get('email')
        print(mail)
        if not SubscribersEmail.objects.filter(email=mail):
            new_sub = SubscribersEmail(email=mail)
            new_sub.save()
            messages.add_message(response, messages.INFO, 'Successfully Subscribed To Our Newsletter.')
            return redirect('home')
        else:
            messages.add_message(response, messages.INFO, 'This Email Is Already Subscribed.')
            return redirect('home')
    
    news = NewsArticle.objects.order_by("-publishedAt")[:30] #.filter(publishedAt=date.today().strftime('%Y-%m-%d'))
    context = {"news": news}
    return render(response, 'frontend/frontend.html', context)

