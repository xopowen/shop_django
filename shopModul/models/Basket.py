from django.db import models
from django.contrib.auth.models import User

from shopModul.models.OrderProduct import OrderProduct


class Basket(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    order_product = models.ManyToManyField(OrderProduct)