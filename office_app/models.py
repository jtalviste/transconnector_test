from django.db import models

from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    office = models.ForeignKey(Office, null=True, default=None, on_delete=models.SET_NULL)

class WorkHistory(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    last_checked = models.DateTimeField()

