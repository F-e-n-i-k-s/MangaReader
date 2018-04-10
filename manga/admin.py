from django.contrib import admin
from achievement.models import *
from manga.models import *
from translater.models import *
from bookmark.models import *

# Register your models here.
admin.site.register(Achievement)
admin.site.register(Translater)
admin.site.register(Bookmark)
#admin.site.register(Author, Genre, Manga, Chapter, Page)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Page)