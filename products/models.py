from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return f"{self.id} | {self.title}"

class Product(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='products/')
    info = models.CharField(max_length=128)
    price = models.PositiveSmallIntegerField()
    
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return f"{self.id} | {self.title}"