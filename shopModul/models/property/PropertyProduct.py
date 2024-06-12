from django.db import models



class PopertyProduct(models.Model):
    property = models.ForeignKey('Property',on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.ForeignKey('PropertyValue', on_delete=models.SET_NULL,null=True)