from django.db import models


class Route(models.Model):
    route_from = models.CharField(max_length=100)
    route_to = models.CharField(max_length=100)
    sacco_name = models.CharField(max_length=100)
    morning_fare = models.IntegerField()
    daytime_fare = models.IntegerField()
    evening_fare = models.IntegerField()

    def __str__(self):
        return self.route_from + ' ---> ' + self.route_to
