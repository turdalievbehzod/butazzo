from django.shortcuts import render
from shared.models import Banner


def home_page_view(request):
    return render(request, 'index.html')


def index(request):
    banners = Banner.objects.filter(is_active=True)

    return render(request, 'index.html', {
        'banners': banners
    })