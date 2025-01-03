"""
Models for core app.
"""

from djongo import models


class Book(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=False, null=False)
    published_date = models.DateField(blank=False, null=False)
    genre = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
