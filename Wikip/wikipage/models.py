import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class author_signup(models.Model):
    aid = models.AutoField(primary_key = True)
    author_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    pswd = models.CharField(max_length=200)
    def __unicode__(self):
        return self.author_name


class article(models.Model):
    article_id = models.AutoField(primary_key = True)
    uid = models.ForeignKey(author_signup)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('Last edited')
    def __unicode__(self):
        return self.title

