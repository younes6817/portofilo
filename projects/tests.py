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

    def test_common_statuses_translate_without_project_specific_mapping(self):
        project = self.create_project(
            title='test',
            title_fa='',
            status='Done',
            status_fa='',
        )

        response = self.client.get(reverse('project:project_detail', args=[project.id]))

        self.assertContains(response, 'data-fa="تست"')
        self.assertContains(response, 'data-fa="تکمیل‌شده"')

    def test_current_live_projects_and_categories_have_persian_fallbacks(self):
        expected_projects = {
            'Liora Cafe': ('کافه لیورا', 'فعال'),
            'Cafe Gavazn': ('کافه گوزن', 'در آستانه شروع'),
            'Personal AI Assistant': ('دستیار هوش مصنوعی شخصی', 'فعال'),
            'Barber shop booking': ('سامانه نوبت‌دهی آرایشگاه', 'در حال توسعه'),
        }
        statuses = {
            'Liora Cafe': 'Live',
            'Cafe Gavazn': 'Coming to start',
            'Personal AI Assistant': 'Live',
            'Barber shop booking': 'Writing',
        }

        for title, (expected_title, expected_status) in expected_projects.items():
            project = self.create_project(
                title=title,
                title_fa='',
                status=statuses[title],
                status_fa='',
                description='English database description',
                description_fa='',
            )
            self.assertEqual(project.title_fa_display, expected_title)
            self.assertEqual(project.status_fa_display, expected_status)
            self.assertNotEqual(project.description_fa_display, project.description)

        expected_categories = {
            'Bots': 'بات‌ها',
            'Client Work': 'پروژه مشتری',
            'Contract': 'قراردادی',
            'For Sale': 'آماده فروش',
            'Personal': 'شخصی',
            'REST API': 'رابط برنامه‌نویسی REST',
        }
        for name, expected_name in expected_categories.items():
            category = Category(name=name)
            self.assertEqual(category.name_fa_display, expected_name)

        feature = ProjectFeature(feature='Gemini AI Integration')
        image = ProjectImage(image_name='Admin Menu')
        stack = TechStack(title='DevOps')
        self.assertEqual(feature.feature_fa_display, 'اتصال به هوش مصنوعی Gemini')
        self.assertEqual(image.image_name_fa_display, 'مدیریت منو')
        self.assertEqual(stack.title_fa_display, 'دواپس')

    def test_known_database_values_have_runtime_persian_fallbacks(self):
        project = self.create_project(
            title='Digital Menu',
            title_fa='',
            status='Demo',
            status_fa='',
            description='English fixture description',
            description_fa='',
            cilend_or_role='freelance',
            cilend_or_role_fa='',
        )
        category = Category.objects.create(name='Backend')
        stack = TechStack.objects.create(title='Django', percent=90, color='#a855f7')
        project.categories.add(category)
        project.tech_stacks.add(stack)
        ProjectFeature.objects.create(project=project, feature='Admin Panel')
        ProjectImage.objects.create(
            project=project,
            type='mobile',
            image='projects/mobile.webp',
            image_name='Login Page',
        )

        list_response = self.client.get(reverse('project:projects'))
        detail_response = self.client.get(reverse('project:project_detail', args=[project.id]))

        self.assertContains(list_response, 'data-fa="منوی دیجیتال"')
        self.assertContains(list_response, 'data-fa="بک‌اند"')
        self.assertContains(detail_response, 'data-fa="نسخه دمو"')
        self.assertContains(detail_response, 'data-fa="جنگو"')
        self.assertContains(detail_response, 'data-fa="پنل مدیریت"')
        self.assertContains(detail_response, 'data-fa="صفحه ورود"')
