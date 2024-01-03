from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    aq_date = models.DateField()
    health_state = models.CharField( max_length=30, default='zdrowy')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    loyalty_points = models.IntegerField

class Reservation(models.Model):
    date = models.DateField()
    hour_from = models.TimeField()
    hour_to = models.TimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Adoption(models.Model):
    date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Playpen(models.Model):
    playpen_number = models.IntegerField
    localization = models.CharField(max_length=300)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

class HealthRecord(models.Model):
    date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    description = models.CharField(max_length=3000)