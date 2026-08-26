from django.db import models
from tech_stack.models import TechStack

class Project(models.Model):
    title = models.CharField(max_length=100)
    image_default = models.ImageField()
    status_percent = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    description = models.TextField()
    important = models.IntegerField(default=1)
    tech_stacks = models.ManyToManyField(TechStack, related_name='projects', blank=True)
    github_link = models.URLField(max_length=255, null=True, blank=True)
    live_demo_link = models.URLField(max_length=255, null=True, blank=True)
    cilend_or_role = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    type = models.CharField(
        max_length=8,
        choices=[
            ('mobile', 'Mobile'),
            ('desktop', 'Desktop')
        ]
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    image_name = models.CharField(max_length=255, null=True, blank=True)

class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    feature = models.TextField()