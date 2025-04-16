from django.db import models

# Create your models here.

class Feedback(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    suggestion = models.TextField()
    date_submitted = models.DateField(auto_now_add=True)
