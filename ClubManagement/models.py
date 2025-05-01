from django.db import models

# Create your models here.

class Tasks(model.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default = False)
    assign_to_user = models.ForeignKey(User, on_delete = models.CASCADE)
    assigned_role = models.CharField(max_length = 50)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

class Skill(models.Model):
  #user class doesnt exsist in this, stand in User
  user_id = models.ForeignKey(Users, max_length=10)
  skill_name = models.CharField(max_length=255)
  proficiency = models.IntegerField()

class Interests(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE),
    interest_name = models.CharField(max_length = 50)

class Documentation(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True) 

class SuggestionTable(models.Model):
    user_id = models.ForeignKey.(Users, max_length = 10)
    user_id = models.ForeignKey.(Users, max_length = 10)
    suggestion = models.TextField()
    date_submitted = models.DateField()

class Feedback(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    suggestion = models.TextField()
    date_submitted = models.DateField(auto_now_add=True)
