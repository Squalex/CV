from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
