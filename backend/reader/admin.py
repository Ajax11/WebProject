from django.contrib import admin

from .models import Author, Chapter, Manga

# Register your models here.

admin.site.register(Author)
admin.site.register(Chapter)
admin.site.register(Manga)
