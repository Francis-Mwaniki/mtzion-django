from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.
class TopicSeries(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField("Topic series", null=True,unique=True, blank=False)
    published = models.DateField("Date published",default=timezone.now)
    
    class Meta:
        verbose_name_plural = "SERIES"
        ordering = ['-published']
    
    def __str__(self):
       return self.title
    
    # @property
    # def __str__(self) -> str:
    #     return self.slug
    
class Topics(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default="",blank=True)
    speaker = models.CharField(max_length=255)
    content =  HTMLField(blank=True, default="")
    topicSlug =models.SlugField("Topic slug",unique=True,blank=False, null=False)
    series = models.ForeignKey(TopicSeries,default="",on_delete=models.SET_DEFAULT)
    published = models.DateTimeField('Date published', default=timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    
    class Meta:
        verbose_name_plural = "TOPICS"
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    @property
    def __str__(self):
        return self.topicSlug
    
    
    def slug(self):
        return self.series.slug + "/" + self.topicSlug
    