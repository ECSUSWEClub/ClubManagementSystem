from django.db import models

class Tasks(model.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default = False)
    assign_to_user = models.ForeignKey(User, on_delete = models.CASCADE)
    assigned_role = models.CharField(max_length = 50)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)