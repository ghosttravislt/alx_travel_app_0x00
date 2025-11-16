# listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            "listing_id",
            "title",
            "description",
            "location",
            "price_per_night",
            "host",
            "created_at",
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "booking_id",
            "user",
            "listing",
            "check_in",
            "check_out",
            "status",
            "created_at",
        ]
