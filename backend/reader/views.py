from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer, MangaSerializer, ChapterSerializer
from .models import Author, Chapter, Manga

# Create your views here.

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class MangaView(viewsets.ModelViewSet):
	serializer_class = MangaSerializer
	queryset = Manga.objects.all()


class ChapterView(viewsets.ModelViewSet):
	serializer_class = ChapterSerializer
	queryset = Chapter.objects.all()
