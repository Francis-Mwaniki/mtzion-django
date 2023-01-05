from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.
class TopicSeries(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField("Topic series", null=True,unique=True, blank=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
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
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
            
    
class Topics(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default="",blank=True)
    speaker = models.CharField(max_length=255)
    content =  HTMLField(blank=True, default="")
    topic_slug =models.SlugField("Topic slug",unique=True,blank=False, null=False)
    series = models.ForeignKey(TopicSeries,default="",on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    published = models.DateTimeField('Date published', default=timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    
    class Meta:
        verbose_name_plural = "TOPICS"
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    
    def slug(self):
        return self.series.slug + "/" + self.topic_slug
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
        
    