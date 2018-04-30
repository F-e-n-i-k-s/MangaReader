from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    photo = models.CharField(max_length=250)


class Genre(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    age_rating = models.IntegerField(default=0)


class Manga(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    rating = models.FloatField(max_length=1)
    poster = models.ImageField(upload_to='upload/manga/', blank=True, verbose_name=title)
    header = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)


class Chapter(models.Model):
    manga_id = models.ForeignKey(Manga, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    volume = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    description = models.TextField()
    rating = models.FloatField(max_length=1)
    date = models.DateField()
    #translater_id =


class Page(models.Model):
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)