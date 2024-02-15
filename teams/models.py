from django.db import models
from authentications.models import User
from issues.models import Issue


class Team(models.Model):
    name = models.CharField(max_length=200)
    auth_code = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name