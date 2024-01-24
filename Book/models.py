from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    reitings = models.IntegerField()
    price = models.FloatField
