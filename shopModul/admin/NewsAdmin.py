from django.contrib import admin

from shopModul.admin.admin import ParagraphInline, FeedbackInfo
from shopModul.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [ParagraphInline,FeedbackInfo]