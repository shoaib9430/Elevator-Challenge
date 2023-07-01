"""Viewset class for Elevator model."""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import Elevator
from api.serializers import ElevatorSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    """Viewset class for Elevator model."""

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['GET'])
    def status(self, request, pk=None, elevator_system=None):
        """Fetch the next destination floor for a given elevator."""
        try:
            elevator = self.queryset.filter(elevator_system=elevator_system).get(pk=pk)
            response = {}
            response['elevator_system'] = elevator_system
            response['data'] = self.get_serializer(elevator).data
            return Response(response)
        except Exception as e:
            return Response({'error': str(e)}, status=404)

    @action(detail=True, methods=['PATCH'])
    def update(self, request, pk=None, elevator_system=None):
        """Update elevator."""
        try:
            elevator = self.queryset.filter(elevator_system=elevator_system).get(pk=pk)
            serializer = self.get_serializer(elevator, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {}
                response['elevator_system'] = elevator_system
                response['data'] = serializer.data
                return Response(response)
        except Exception as e:
            return Response({'error': str(e)}, status=404)
