

from django.db import models
from django.utils.translation import gettext_lazy as _

from shopModul.models.News import News


class Paragraph(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    position_img = models.CharField(max_length=20,choices=[('l', 'left'),('R',"right")],default='l')
    img = models.ImageField(blank=True,null=True,upload_to='img/paragraph/%Y/%m/%d/')
    text = models.TextField()

    def __str__(self):
        return "Paragraph " + self.news.__str__()

    class Meta:
        verbose_name = _("Paragraph")
        verbose_name_plural = _("Paragraphs")
