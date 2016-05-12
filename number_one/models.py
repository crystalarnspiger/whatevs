from django.db import models
from django.core.exceptions import ValidationError


class Person(models.Model):

    nn_id = models.CharField(unique=True, max_length=8)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


