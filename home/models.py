from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os
# Create your models here.
class TopicSeries(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField("Topic series", null=True,unique=True, blank=False)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
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
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default="",blank=True)
    speaker = models.CharField(max_length=255)
    content =  HTMLField(blank=True, default="")
    topic_slug =models.SlugField("Topic slug",unique=True,blank=False, null=False)
    series = models.ForeignKey(TopicSeries,default="",on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/user.png'  upload_to=image_upload_to,max_length=255)
    published = models.DateTimeField('Date published', default=timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    
    class Meta:
        verbose_name_plural = "TOPICS"
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    
    def slug(self):
        return self.series.slug + "/" + self.topic_slug
    