from datetime import timezone
from django.conf import settings
from django.db import models

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(settings.BLOG_POST_MODEL, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text