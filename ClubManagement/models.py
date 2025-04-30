from django.db import models

# Create your models here.

class SurveyQuestions(models.Model):

    QUESTION_TYPES = {
        "multiple-choice" : "Multiple Choice",
        "text" : "Text",
        "checkbox" : "Checkbox",
        "dropdown" : "Dropdown",
        "true-false" : "True or False"
    }

    survey_id = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default="text")