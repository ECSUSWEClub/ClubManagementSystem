from django.db import models

class Surveys(models.model):
    title = models.Charfield(max_length=50),
    created_by = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)