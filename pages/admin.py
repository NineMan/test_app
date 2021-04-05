from django.contrib import admin

from .models import Audio
from .models import Page
from .models import Text
from .models import Video


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    search_fields = ["title", "content__title"]
    filter_horizontal = ["content"]


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ("title", "bitrate", "counter")
    search_fields = ["title"]


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("title", "content_text", "counter")
    search_fields = ["title"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "url_video", "url_subtitles", "counter")
    search_fields = ["title"]
