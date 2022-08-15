from django.http import HttpResponse
from django.shortcuts import render


def index(response):
    return render(response, 'frontend/index.html', {})
