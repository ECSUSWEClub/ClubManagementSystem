import django.db
from datetime import date
#thing for Enum
parameters = ['Present','Excused','Absent',]

class Meeting(models.Model):
    #fields
    date = models.DateField()
    location = models.CharField()
    attendees_count = model.IntegerField()
    club_season_id = models.IntegerField(Club)

    def __str__(self):
        return self.name
