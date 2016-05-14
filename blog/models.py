from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) # blank表示网页中的表单可以为空, null表示数据库中的该字段可以为空

    def publish(self):
        self.published_date = timezone.now()  # 默认self含有以上的全部字段?
        self.save()

    def __str__(self):
        return self.title
