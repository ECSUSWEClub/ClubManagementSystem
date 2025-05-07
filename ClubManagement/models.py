from django.db import models

class Club(models.Model):
    SEMESTER = {
        "F": "Fall",
        "W": "Winter"
    }
    semester = models.CharField(max_length=1, choices=SEMESTER)
    year = models.IntegerField()
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()


# Create your models here.
