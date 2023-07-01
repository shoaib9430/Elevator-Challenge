"""Model class for Elevator Requests"""

from django.db import models
from api.models.base_model import BaseModel

class ElevatorRequest(BaseModel):
    """Model class for Elevator Requests"""

    elevator = models.ForeignKey('Elevator', on_delete=models.CASCADE)
    requested_from_floor = models.IntegerField()
    requested_to_floor = models.IntegerField()
    is_serviced = models.BooleanField(default=True)

    def __str__(self):
        return self.elevator + " requested from floor " + self.requested_from_floor

    class Meta:
        """Meta class for Elevator Requests"""
        db_table = 'elevator_request'
        ordering = ['elevator']
        verbose_name_plural = 'elevator_requests'