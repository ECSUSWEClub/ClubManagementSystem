from django.db import models

#model class
class EmailList(models.Model):
    #fields
    id=models.IntegerField()
    user_id=models.IntegerField()
    club_season_id=models.IntegerField()
    subscribed=models.BooleanField()
    #Stack overflow had this, I assume it returns readable name of class
    def __str__(self):
        return self.name
