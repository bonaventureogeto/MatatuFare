from django.db import models


class Contact(models.Model):
    route_from = models.CharField(max_length=100)
    route_to = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.route_to
