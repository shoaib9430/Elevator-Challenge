"""Viewset for ElevatorSystem"""
from django.db.models import F, Func

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ElevatorSystemSerializer, ElevatorRequestSerializer
from api.models import ElevatorSystem, Elevator


class ElevatorSystemViewSet(viewsets.ModelViewSet):
    """Viewset for ElevatorSystem"""

    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

    @action(detail=False, methods=['GET'])
    def by_system_name(self, request, system_name=None):
        try:
            elevator_system = ElevatorSystem.objects.get(system_name=system_name)
            serializer = self.get_serializer(elevator_system)
            return Response(serializer.data)
        except ElevatorSystem.DoesNotExist:
            return Response({'error': 'Elevator system not found.'}, status=404)

    @action(detail=True, methods=['POST'])
    def request_elevator(self, request, pk=None):
        try:
            elevator_system = self.get_object()
            serializer = ElevatorRequestSerializer(data=request.data)

            requested_from_floor = serializer.initial_data['requested_from_floor']
            requested_to_floor = serializer.initial_data['requested_to_floor']

            # This query gets the closest elevator to the requested floor using Order By and ABS function
            closest_elevator = Elevator.objects.filter(elevator_system=elevator_system, is_operational=True).annotate(
                distance=Func(F('current_floor') - requested_from_floor, function='ABS')).order_by('distance').first()

            if closest_elevator:
                # Save properties to the closest elevator
                direction = (requested_to_floor - requested_from_floor) / abs(requested_to_floor - requested_from_floor)
                closest_elevator.direction = direction
                closest_elevator.current_floor = requested_to_floor
                closest_elevator.save()

                serializer.initial_data['elevator'] = closest_elevator.id

                if serializer.is_valid():
                    elevator_request = serializer.save()

                    return Response(ElevatorRequestSerializer(elevator_request).data)

        except ElevatorSystem.DoesNotExist:
            return Response({'error': 'Elevator system not found.'}, status=404)

        except Exception as e:
            return Response({'error': str(e)}, status=400)
