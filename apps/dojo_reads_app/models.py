from django.db import models
from apps.login_register_app.models import User

# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, related_name='book', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField(default=0)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    poster = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)