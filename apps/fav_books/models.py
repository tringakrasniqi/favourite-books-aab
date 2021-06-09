from django.db import models
from apps.authenticate.models import User


class Book(models.Model):
    """
        Klasa Book e krijon nje tablele ne databazen e aplikacionit qe permbat te dhenat e librit. Ne kete table kemi dhe foreignKey qe e nenkupton lidhen nje-me-shume (one-to-many) me tablen User.
    """
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    isbn_number = models.IntegerField()
    published_year = models.DateField(auto_now=False, auto_now_add=False)
    of_user = models.ForeignKey(
        User, related_name="has_books", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
