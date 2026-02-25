from django.contrib import admin

# Register your models here.

from shared.models import Banner
from .models import Banner, Gallery

admin.site.register(Banner)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


