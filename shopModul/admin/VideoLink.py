from django.contrib import admin

from shopModul.models import VideoLink


@admin.register(VideoLink)
class VideoLinkAdmin(admin.ModelAdmin):
    model = VideoLink