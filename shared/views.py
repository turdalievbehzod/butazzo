from django.shortcuts import render
from shared.models import Banner, Gallery


def home_page_view(request):
    banners = Banner.objects.order_by('created_at')
    gallery = Gallery.objects.all()

    return render(request, 'index.html', {
        'banners': banners,
        'gallery': gallery,
    })