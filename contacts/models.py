from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    route_from = models.CharField(max_length=100, default=True)
    route_to = models.CharField(max_length=100, default=True)
    fare = models.CharField(max_length=100, default=0)
    sacco_name = models.CharField(max_length=100, default=True)
    message = models.TextField(blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
