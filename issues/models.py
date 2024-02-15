from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField()
    chatGPT_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    author = models.ForeignKey('authentications.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title