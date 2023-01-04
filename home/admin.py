from django.contrib import admin
from .models import Topics, TopicSeries

# Register your models here.
class TopicSeriesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "slug",
        'author',
        'image',
        "published"
    ]
class TopicsAdmin(admin.ModelAdmin):
       fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "topic_slug", "series",'author','image']}),
        ("Content", {"fields": ["content", "speaker"]}),
        ("Date", {"fields": ["modified"]})
    ]
admin.site.register( TopicSeries, TopicSeriesAdmin)
admin.site.register( Topics, TopicsAdmin)