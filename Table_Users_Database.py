
from django.db import models

class Table_users(models.Model): 
    first_name = models.CharField(max_length= 50),
    last_name = models.CharField(max_length= 50),
    member_username = models.CharField(max_length= 50),
    discord_username = models.CharField(max_length= 50),
    github_username = models.CharField(max_length= 50),
    email = models.CharField(max_length=50),
    role = models.CharField(max_length= 50, choices= [
     ('MEMBER', 'Member'),  
     ('PRESIDENT', 'President'),
     ('VICE PRESIDENT', 'Vice President'),
     ('PUBLIC RELATIONS OFFICER', 'Public Relations Officer'),
     ('TREASURER', 'Treasurer'),
     ('SECRETARY', 'Secretary')
    ])
    password = models.CharField(max_length=128)
    date_joined = models.DateField(auto_now_add=True)
    active = models.BooleanField(),
    alumni = models.BooleanField(),
    
    club = models.ForeignKey(Club, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"