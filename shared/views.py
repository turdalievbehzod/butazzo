from django.shortcuts import render
from shared.models import Banner


def home_page_view(request):
    banners = Banner.objects.order_by('-created_at')

    return render(request, 'index.html', {
        'banners': banners
    })
