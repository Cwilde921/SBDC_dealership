from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return str(self.make) + " " + str(self.model)
        
    def __iter__(self):
        return iter([self.make, self.model, self.color, self.price])