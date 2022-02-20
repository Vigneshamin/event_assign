from django.db import models
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True,max_length=200)
    email = models.CharField(null=True,max_length=200)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Cancelled', 'Cancelled'),
    )
    name = models.CharField(null=True,max_length=200)
    description = models.CharField(null=True,max_length=1000)
    maxticket = models.IntegerField(null=True)
    remticket = models.IntegerField(null=True)
    event_date = models.DateTimeField(null=True, default=date.today()+timedelta(days=10))
    price = models.FloatField(null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS, default='Active')

    def __str__(self):
        return self.name

class Bookings(models.Model):
    STATUS = (
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True,on_delete=models.SET_NULL)
    no_ticket = models.IntegerField(null=True,)
    date_created = models.DateTimeField(null=True)
    status = models.CharField(max_length=100,null=True, choices=STATUS, default='Booked')

    def __str__(self):
        return self.event.name
