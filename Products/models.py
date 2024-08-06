from django.db import models
from django.utils import timezone
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=52)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    description = models.TextField()
    order_date = models.DateTimeField(default=timezone.now)
    # image = models.ImageField(upload_to='media',default='default.jpg')


    def __str__(self):
        return self.name