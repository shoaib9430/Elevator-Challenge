from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import Elevator, ElevatorRequest
from api.serializers import ElevatorRequestSerializer

class ElevatorRequestViewSet(viewsets.ModelViewSet):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer

    @action(detail=True, methods=['GET'])
    def requests_for_elevator(self, request, pk=None, elevator_system=None):
        try:
            elevator = Elevator.objects.filter(elevator_system=elevator_system).get(pk=pk)
            requests = self.queryset.filter(elevator=elevator)
            serializer = self.get_serializer(requests, many=True)
            return Response(serializer.data)
        except Elevator.DoesNotExist:
            return Response({'error': 'Elevator not found.'}, status=404)
