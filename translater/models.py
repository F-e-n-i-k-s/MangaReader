from django.db import models


class Translater(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    translate_rating = models.FloatField(max_length=1)
    clean_rating = models.FloatField(max_length=1)
    type_rating = models.FloatField(max_length=1)