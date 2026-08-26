from django.db import models

class TechStack(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField()
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.title
