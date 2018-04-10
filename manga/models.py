from django.db import models


class Manga(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    rating = models.FloatField(max_length=1)
    poster = models.CharField()
    header = models.CharField()
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)


class Genre(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    age_rating = models.IntegerField(max_length=2)


class Author(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    photo = models.CharField()


class Chapter(models.Model):
    manga_id = models.ForeignKey(Manga)
    title = models.CharField(max_length=250)
    volume = models.IntegerField(max_length=4)
    number = models.IntegerField(max_length=6)
    description = models.TextField()
    rating = models.FloatField(max_length=1)
    date = models.DateField()
    #translater_id =


class Page(models.Model):
    chapter_id = models.ForeignKey(Chapter)
    number = models.IntegerField(max_length=4)