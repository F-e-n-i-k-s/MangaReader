from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=250)