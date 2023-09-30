from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length= 100, unique=True)
    description = models.TextField(max_length= 500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photos/products', null=True, blank=True)
    location = models.CharField(max_length=100, default='YourDefaultLocation')

    def __str__(self):
        return self.hotel_name
