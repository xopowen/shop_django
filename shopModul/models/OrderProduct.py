from django.db import models

from shopModul.models import Product


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amt = models.IntegerField(default=1)
    issued = models.BooleanField(default=False)

