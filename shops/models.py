from django.contrib.gis.db import models



class Shop(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
