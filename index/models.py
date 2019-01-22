from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    content = models.CharField('内容', max_length = 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    update_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.content
