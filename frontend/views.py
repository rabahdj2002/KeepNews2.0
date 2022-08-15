from django.shortcuts import render


def index(response):
    return render(response, 'frontend/index.html', {})
