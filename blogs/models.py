from django.db import models

# Create your models here.
# posts/models.py
from django.conf import settings
from django.db import models


class Post(models.Model):

    title=models.CharField(max_length=256)
    description=models.TextField()
    status=models.BooleanField(default=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title