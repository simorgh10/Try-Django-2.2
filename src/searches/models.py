from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class SearchQuery(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)
