from django.test import TestCase
from django.urls import reverse

from .models import Project


class ProjectDetailFallbackTests(TestCase):
    def create_project(self, **overrides):
        values = {
            'title': 'Portfolio project',
            'image_default': 'projects/test.webp',
            'status_percent': 75,
            'status': 'In progress',
            'description': 'Project description',
            'important': 1,
            'is_active': True,
        }
        values.update(overrides)
        return Project.objects.create(**values)

    def test_active_project_opens_its_detail_page(self):
        project = self.create_project()

        response = self.client.get(
            reverse('project:project_detail', args=[project.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_detail.html')
        self.assertEqual(response.context['project'], project)

    def test_missing_project_redirects_to_project_list(self):
        response = self.client.get(
            reverse('project:project_detail', args=[999999])
        )

        self.assertRedirects(response, reverse('project:projects'))

    def test_inactive_project_redirects_to_project_list(self):
        project = self.create_project(is_active=False)

        response = self.client.get(
            reverse('project:project_detail', args=[project.id])
        )

        self.assertRedirects(response, reverse('project:projects'))
