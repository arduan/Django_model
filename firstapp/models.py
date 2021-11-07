from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    # DoesNotExist = models.Manager


class Company(models.Model):
    name = models.CharField(max_length=30)

# Создание модели один ко многим.
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
