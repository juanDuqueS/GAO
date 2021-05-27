from django.db import models

# Create your models here.

class Stock(models.Model):
    item = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'stock')
    createdAt = models.DateField(auto_now_add = True)
    updatedAt = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.item

class Providers(models.Model):
    name = models.CharField(max_length = 30)
    createdAt = models.DateField(auto_now_add = True)
    updatedAt = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
    
    def __str__(self):
        return self.name