from django.db import models
from datetime import datetime


class Crud(models.Model):
    title = models.CharField(max_length=100, default='Product without title')
    model = models.CharField(max_length=100, default='Product without model')
    price = models.FloatField(default=0.0)
    discription = models.TextField(default='')
    quantity = models.IntegerField(default=0)
    activation = models.BooleanField(default=False)
    image = models.TextField(default='')

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Price: {self.price}, Quantity: {self.quantity}, Activation: {self.activation}'


class Comment(models.Model):
    # коментарі, які у випадку видалення продукта будуть також всі видалені
    product = models.ForeignKey(Crud, on_delete=models.CASCADE)
    comment_text = models.CharField('тест комментария', max_length=200)

    def __str__(self):
        return f'Text: {self.comment_text}'


class Cart(models.Model):
    session_id = models.TextField(default='')
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.session_id}, {self.count}, {self.total}'


class Entry(models.Model):
    product = models.ForeignKey(Crud, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()