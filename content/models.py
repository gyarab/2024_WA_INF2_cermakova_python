
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth = models.TextField()
    image = models.URLField()
    bio = models.TextField()

    def __str__(self):    
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):    
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.URLField()
    year = models.TextField()
    link = models.URLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")  # 1:N
    genres = models.ManyToManyField(Genre, related_name="books")  # M:N

    def __str__(self):    
        return self.title
