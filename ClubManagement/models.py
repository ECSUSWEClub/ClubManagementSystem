from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=100)
    club_session_id = models.ForeignKey(Club)