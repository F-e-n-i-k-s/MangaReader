from django.db import models
from manga.models import Page


class Bookmark(models.Model):
    '''user_id'''
    page_id = models.ManyToManyField(Page)
    title = models.CharField(max_length=250)