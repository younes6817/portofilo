from django.test import TestCase
from django.urls import reverse

from tech_stack.models import TechStack

from .models import Category, Project, ProjectFeature, ProjectImage


class ProjectDetailFallbackTests(TestCase):
    def create_project(self, **overrides):
        values = {
            'title': 'Portfolio project',
            'title_fa': 'پروژه پورتفولیو',
            'image_default': 'projects/test.webp',
            'status_percent': 75,
            'status': 'In progress',
            'status_fa': 'در حال توسعه',
            'description': 'Project description',
            'description_fa': 'توضیحات پروژه',
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
        self.assertContains(response, 'data-page-title-fa="پروژه پورتفولیو — یونس"')
        self.assertContains(response, 'data-language-content="fa"')
        self.assertContains(response, 'توضیحات پروژه')

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

    def test_persian_database_content_is_available_on_list_and_detail_pages(self):
        project = self.create_project(cilend_or_role='Backend Developer', cilend_or_role_fa='توسعه‌دهنده بک‌اند')
        category = Category.objects.create(name='Backend', name_fa='بک‌اند')
        stack = TechStack.objects.create(title='Django', title_fa='جنگو', percent=90, color='#a855f7')
        project.categories.add(category)
        project.tech_stacks.add(stack)
        ProjectFeature.objects.create(project=project, feature='Authentication', feature_fa='احراز هویت')
        ProjectImage.objects.create(
            project=project,
            type='mobile',
            image='projects/mobile.webp',
            image_name='Login page',
            image_name_fa='صفحه ورود',
        )

        list_response = self.client.get(reverse('project:projects'))
        detail_response = self.client.get(reverse('project:project_detail', args=[project.id]))

        self.assertContains(list_response, 'data-fa="پروژه پورتفولیو"')
        self.assertContains(list_response, 'data-fa="بک‌اند"')
        self.assertContains(detail_response, 'data-fa="جنگو"')
        self.assertContains(detail_response, 'data-fa="احراز هویت"')
        self.assertContains(detail_response, 'data-fa="صفحه ورود"')
        self.assertContains(detail_response, 'data-fa="توسعه‌دهنده بک‌اند"')
