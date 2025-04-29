from django.db import models

# Create your models here.
class SuggestionTable(models.Model):
    user_id = models.IntegerField()
    suggestion = models.TextField()
    date_submitted = models.DateField()
