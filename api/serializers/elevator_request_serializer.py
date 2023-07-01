"""Serializer for ElevatorRequest"""
from rest_framework import serializers
from api.models import ElevatorRequest

class ElevatorRequestSerializer(serializers.ModelSerializer):
    """Serializer for ElevatorRequest"""

    class Meta:
        model = ElevatorRequest
        fields = ['elevator', 'requested_from_floor', 'requested_to_floor', 'is_serviced']
