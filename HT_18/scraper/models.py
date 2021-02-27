from django.db import models


# Create your models here.


class Product(models.Model):
    url = models.TextField(default="")
    discription = models.TextField(default="None", max_length=1000)
    name = models.TextField(default="Without name", max_length=50)
    phone_number = models.TextField(default="Without number", max_length=50)

    def __str__(self):
        return f'URL: {self.url}, Discription: {self.discription}, Author name: {self.name}, Phone number: {self.phone_number}'
