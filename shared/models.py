from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    discount = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Gallery {self.id}"

    class Meta:
        ordering = ['created_at']