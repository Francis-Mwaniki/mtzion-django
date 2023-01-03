from django.contrib import admin
from .models import Topics, TopicSeries

# Register your models here.
class TopicSeriesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "slug",
        "published"
    ]
class TopicsAdmin(admin.ModelAdmin):
    fields = [
      "title",
        "subtitle",
        "topicSlug",
        "content",
         "speaker",
        "published",
        "modified",
        "series"
    ]
admin.site.register( TopicSeries, TopicSeriesAdmin)
admin.site.register( Topics, TopicsAdmin)