"""Model class for Elevator"""

from django.db import models
from api.models.base_model import BaseModel


class Elevator(BaseModel):
    """Model class for Elevator"""
    elevator_system = models.ForeignKey('ElevatorSystem', on_delete=models.CASCADE)
    elevator_number = models.IntegerField()
    current_floor = models.IntegerField(default=1)
    is_door_open = models.BooleanField(default=True)
    direction = models.CharField(choices=[(1, 'UP'), (-1, 'DOWN'), (0, 'STANDING STILL')], default=0)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return self.elevator_number

    class Meta:
        """Meta class for Elevator"""

        db_table = 'elevator'
        ordering = ['elevator_number']
        verbose_name_plural = 'elevators'
