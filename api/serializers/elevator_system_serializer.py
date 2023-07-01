"""Serializer for ElevatorSystem"""

from rest_framework import serializers
from api.models import ElevatorSystem, Elevator
from api.serializers import ElevatorSerializer

class ElevatorSystemSerializer(serializers.ModelSerializer):
    """Serializer for ElevatorSystem"""

    elevators = serializers.SerializerMethodField()

    class Meta:
        """Meta class for ElevatorSystem"""
        model = ElevatorSystem
        exclude = ('created_at', 'updated_at')

    def get_elevators(self, obj):
        elevators = Elevator.objects.filter(elevator_system=obj)
        return ElevatorSerializer(elevators, many=True).data

    def create(self, validated_data):
        """Overriding create method to create elevators for the elevator system"""

        elevator_system = ElevatorSystem.objects.create(**validated_data)
        number_of_elevators = validated_data.get('number_of_elevators')

        if number_of_elevators:
            for elevator_number in range(1, number_of_elevators + 1):
                Elevator.objects.create(elevator_system=elevator_system, elevator_number=elevator_number)

        return elevator_system
