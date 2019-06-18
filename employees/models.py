from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=500)
    dept = models.CharField(max_length=50)
    photo = models.CharField(max_length=2083)

