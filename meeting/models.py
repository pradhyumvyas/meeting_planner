from django.db import models
from datetime import time


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=250)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} meeting on {self.floor_number} floor at {self.room_number} Room Number"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(10))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.title} at {self.date} on {self.start_time} for {self.duration} hours"
        return self.title
