import datetime
from django.db import models

from django.utils import timezone


class Crud(models.Model):
    title = models.CharField(max_length=100, default='Product without title')
    model = models.CharField(max_length=100, default='Product without model')
    price = models.FloatField(default=0.0)
    discription = models.TextField(default='')
    quantity = models.IntegerField(default=0)
    activation = models.BooleanField(default=False)
    image = models.TextField(default='')

    # publication_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Price: {self.price}, Quantity: {self.quantity}, Activation: {self.activation}'

    # def was_published_last_week(self):
    #     return self.publication_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    # коментарі, які у випадку видалення продукта будуть також всі видалені
    product = models.ForeignKey(Crud, on_delete=models.CASCADE)
    comment_text = models.CharField('тест комментария', max_length=200)

    def __str__(self):
        return f'Text: {self.comment_text}'
