from django.db import models
from authentications.models import User
from issues.models import Issue


class Team(models.Model):
    name = models.CharField(max_length=200)
    auth_code = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    

class Issue(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField()
    chatGPT_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ManyToManyField(Team, related_name='issues')
    author = models.ForeignKey('authentications.User', on_delete=models.CASCADE, related_name='issues')
