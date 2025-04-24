from django.db import models


class Interests(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE),
    interest_name = models.CharField(max_length = 50)

 