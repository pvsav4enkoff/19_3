from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length= 100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TimeField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    def __str__(self):
        return self.title