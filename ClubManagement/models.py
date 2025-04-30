from django.db import models

# Create your models here.
class Skill(models.Model):
  #user class doesnt exsist in this, stand in User
  user_id = models.ForeignKey(User, max_length=10)
  skill_name = models.CharField(max_length=255)
  proficiency = models.IntegerField()

class DocumentationSections(models.Model):
  documentation_id = models.ForeignKey(Documentation, max_length=10)
  section_title = models.CharField(max_length=255)
  section_text = models.TextField()