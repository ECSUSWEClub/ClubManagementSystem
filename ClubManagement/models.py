from django.db import models

# Create your models here.
class SuggestionTable(models.Model):
    user_id = models.ForeignKey.IntegerField(User, max_length = 10)
    suggestion = models.TextField()
    date_submitted = models.DateField()
