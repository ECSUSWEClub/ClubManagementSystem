from django.db import models

class Documentation(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    last_edited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 