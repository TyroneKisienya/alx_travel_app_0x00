from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Listing(models.Model):
    property_id = models.UUIDField(primary_key=True,default=uuid.uuid4, max_length=50)
    host_id = models.CharField(max_length=50)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=128)
    pricepernight = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    property_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    class statType(models.TextChoices):
        PENDING = 'Pending', 'pending'
        CONFIRMED = 'Confirmed', 'confirmed'
        CANCELED = 'Canceled', 'canceled'
    status = models.CharField(choices=statType, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=128)
    property_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

