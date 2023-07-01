"""Model class for Elevator system"""

from django.db import models
from api.models.base_model import BaseModel

class ElevatorSystem(BaseModel):
    """Model class for Elevator system"""

    system_name = models.CharField(max_length=100)
    number_of_elevators = models.IntegerField(default=1)
    number_of_floors = models.IntegerField(default=1)

    def __str__(self):
        return self.system_name

    class Meta:
        """Meta class for Elevator system"""

        db_table = 'elevator_system'
        ordering = ['number_of_elevators']
        verbose_name_plural = 'elevator_systems'