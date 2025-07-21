from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    role_options = [
        ('main','Lead Author'),
        ('supp','Assistant'),
    ]
    role = models.CharField(max_length=10, choices=role_options, default='main')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Manga(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    chapter_number = models.PositiveSmallIntegerField()
    directory_path = models.CharField(max_length=300)
    upload_date = models.DateTimeField(auto_now=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    def __str__(self):
        return f"Chapter number {self.chapter_number}"

