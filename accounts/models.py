from django.conf import settings
from django.db import models
from django.contrib.auth.models import User





class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    more_description = models.CharField(null =True, max_length=500)
