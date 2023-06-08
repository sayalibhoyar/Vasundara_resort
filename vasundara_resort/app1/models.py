from django.db import models

# Create your models here.
class Booking_info(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    mobile = models.IntegerField()
    rooms   = models.IntegerField()
    persons  = models.IntegerField()
    checkin = models.DateField()
    checkout = models.DateField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name
