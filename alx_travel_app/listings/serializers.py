from rest_framework import serializers
from .models import Listing, Booking

class listingSerializer(serializers.ModelSerializer):
    class meta:
        model = Listing
        fields = (
            'property_id',
            'host_id',
            'name',
            'description',
            'pricepernight'
            'created_at'
        )
        read_only_fields = (
            'property_id',
            'host_id',
            'description',
            'pricepernight',
        )

class bookingSerializer(serializers.ModelSerializer):
    class meta:
        model = Booking
        fields = (
            'booking_id',
            'property_id',
            'start_date',
            'end_date'
            'status',
            'created_at'
        )
        read_only_fields = (
            'property_id',
            'created_at',
        )
        extra_kwargs = {
            'status': {'default': Booking.statType.PENDING}
        }