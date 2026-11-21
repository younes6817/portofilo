from django.test import TestCase
from django.urls import reverse

from projects.models import Project
from tech_stack.models import TechStack


class HomePageTests(TestCase):
    def setUp(self):
        self.stack = TechStack.objects.create(
            title='Django',
            title_fa='جنگو',
            percent=90,
            color='#a855f7',
        )

    def create_project(self, title, importance, is_active=True):
        project = Project.objects.create(
            title=title,
            title_fa=f'پروژه {importance}',
            image_default='project.jpg',
            status_percent=80,
            status='In progress',
            status_fa='در حال توسعه',
            description='A useful web product with a clear workflow.',
            description_fa='یک محصول وب کاربردی با جریان کاری روشن.',
            important=importance,
            is_active=is_active,
        )
        project.tech_stacks.add(self.stack)
        return project

    def test_home_shows_only_three_highest_priority_active_projects(self):
        for importance in range(1, 5):
            self.create_project(f'Project {importance}', importance)
        self.create_project('Hidden project', 99, is_active=False)

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        featured = list(response.context['featured_projects'])
        self.assertEqual([project.title for project in featured], [
            'Project 4',
            'Project 3',
            'Project 2',
        ])
        self.assertNotContains(response, 'Hidden project')

    def test_home_keeps_hero_and_adds_clear_section_navigation(self):
        response = self.client.get(reverse('home'))

        self.assertContains(response, 'aria-label="YOUNES"')
        self.assertContains(response, 'data-fa-aria="یونس"')
        self.assertContains(response, 'data-language-content="fa">یونس</span>')
        self.assertContains(response, '<style>.portfolio-v2 {')
        self.assertContains(response, "document.documentElement.classList.add('has-home-motion')")
        self.assertNotContains(response, '/static/css/home-content.css')
        self.assertNotContains(response, '/static/js/home-content.js')
        self.assertContains(response, 'href="#about"')
        self.assertContains(response, 'href="#expertise"')
        self.assertContains(response, 'href="#selected-work"')
        self.assertContains(response, 'href="#contact"')

    def test_language_switcher_and_persian_database_content_are_rendered(self):
        self.create_project('Translated project', 10)

        response = self.client.get(reverse('home'))

        self.assertContains(response, 'id="language-toggle"')
        self.assertContains(response, "sessionStorage.getItem('portfolio-language')")
        self.assertContains(response, 'data-fa="پروژه 10"')
        self.assertContains(response, 'data-fa="جنگو"')
        self.assertContains(response, 'data-fa="یک محصول وب کاربردی با جریان کاری روشن."')

    def test_known_database_values_get_persian_fallbacks_when_fields_are_blank(self):
        self.stack.title_fa = ''
        self.stack.save(update_fields=['title_fa'])
        project = Project.objects.create(
            title='Digital Menu',
            image_default='project.jpg',
            status_percent=100,
            status='Demo',
            description='English fixture description',
            important=10,
            is_active=True,
        )
        project.tech_stacks.add(self.stack)

        response = self.client.get(reverse('home'))

        self.assertContains(response, 'data-fa="منوی دیجیتال"')
        self.assertContains(response, 'data-fa="نسخه دمو"')
        self.assertContains(response, 'data-fa="جنگو"')
