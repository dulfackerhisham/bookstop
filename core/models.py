from django.db import models


"""
    MIGRATIONS are django's way of propagating changes, that we make to our models into our database schema
"""

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title