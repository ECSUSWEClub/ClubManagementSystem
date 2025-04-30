import django.db

#thing for Enum
parameters = ['Present','Excused','Absent',]

class Attendance(models.Model):
    #fields
    meeting_id = models.IntegerField(Meeting)
    user_id = models.IntegerField(Users)
    status = models.CharField(max_length = 1, choices = parameters)

    def __str__(self):
        return self.name
