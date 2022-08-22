from django.db import models

class Trip(models.Model):

    # origin =models.CharField(max_length=64)
    # destination = models.CharField(max_length=64)
    # nights = models.IntegerField()
    # price = models.IntegerField()

    cname = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='Nairobi')
    session = models.CharField(max_length=255, default='')
    

    def __str__(self):
        return f"{self.id} - {self.cname} To {self.country} for {self.city} nights, costs {self.session} EUR"