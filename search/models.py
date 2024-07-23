# search/models.py

from django.db import models


class Search(models.Model):
    search_name = models.fields.CharField(max_length=100)

class Book(models.Model):
    book_name = models.fields.CharField(max_length=100)
    author_name = models.fields.CharField(max_length=50)
    in_stock = models.fields.BooleanField()
    is_digital = models.fields.BooleanField()
    digital_price = models.fields.FloatField(max_length=5)
    is_printed = models.fields.BooleanField()
    printed_price = models.fields.FloatField(max_length=5)
    image_link = models.fields.URLField()

# Create your models here.
