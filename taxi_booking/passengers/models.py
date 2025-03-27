from django.db import models

# Create your models here.

class Passenger(models.Model):
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Booking(models.Model):
    pick_up_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.pick_up_location + " to " + self.destination
