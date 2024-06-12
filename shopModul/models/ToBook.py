from django.db import models
from django.contrib.auth.models import User
from shopModul.models import Event


class ToBook(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=(('accept','accept'),('reject','reject')))
    def __str__(self):
        return F"{self.event.name}: {self.user.get_full_name()} :{self.status} "