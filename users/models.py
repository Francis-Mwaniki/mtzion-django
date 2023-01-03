from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    
    STATUS=(
        ("regular", "regular"),
        ("subscriber", "subscriber"),
        ("moderator","moderator")
    )
    
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100,choices=STATUS, default='regular')
    description = models.CharField(max_length=600,blank=True,default="")
    
    
    def __str__(self):
        return self.username