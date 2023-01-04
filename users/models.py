from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.utils import timezone
# Create your models here.
class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
class CustomUser(AbstractUser):
    
    STATUS=(
        ("regular", "regular"),
        ("subscriber", "subscriber"),
        ("moderator","moderator")
    )
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100,choices=STATUS, default='regular')
    description = models.CharField(max_length=600,blank=True,default="")
    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)
    
    
    def __str__(self):
        return self.username