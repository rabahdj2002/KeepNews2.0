from django.urls import path
from django.shortcuts import redirect
from backend.views import home, newsList, deleteNewsArticle, editNewsArticle, emailsList, deleteEmails, sendEmails, userLogin, userLogout, userForgotPwd, resetPassword


urlpatterns = [
    path('', lambda request: redirect('dashboard/', permanent=False)),
    path('dashboard/', home, name='home'),

    path('login/', userLogin, name='user_login'),
    path('logout/', userLogout, name='user_logout'),
    path('forgot_pwd/', userForgotPwd, name='user_forgot_pwd'),
    path('reset_password/<str:hash>/', resetPassword, name='user_reset_password'),

    path('news/', newsList, name='news_list'),
    path('news/delete/<int:id>/', deleteNewsArticle, name='delete_news_article'),
    path('news/edit/<int:id>/', editNewsArticle, name='edit_news_article'),

    path('emails/', emailsList, name='emails_list'),
    path('emails/delete/<int:id>/', deleteEmails, name='delete_email'),
    path('emails/send/<int:id>/', sendEmails, name='send_email'),
]

handler404 = 'frontend.views.handler404'