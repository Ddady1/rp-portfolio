# listings/models.py

from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

class listing(models.Model):
    title = models.fields.CharField(max_length=100)