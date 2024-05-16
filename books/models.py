# books/models.py


from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    image_link = models.URLField()
    is_digital = models.BooleanField()
    digital_price = models.FloatField(max_length=5)
    is_printed = models.BooleanField()
    printed_price = models.FloatField(max_length=5)



# Create your models here.
