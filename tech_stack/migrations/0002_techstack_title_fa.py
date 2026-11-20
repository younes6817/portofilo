from django.db import migrations, models


TECH_TRANSLATIONS = {
    'Python': 'پایتون',
    'HTML': 'HTML',
    'JavaScript': 'جاوااسکریپت',
    'Tailwind CSS': 'تیلویند CSS',
    'Django': 'جنگو',
    'SQL': 'SQL',
    'REST API': 'REST API',
    'GitHub': 'گیت‌هاب',
}


def populate_persian_titles(apps, schema_editor):
    TechStack = apps.get_model('tech_stack', 'TechStack')
    for stack in TechStack.objects.all():
        translated = TECH_TRANSLATIONS.get(stack.title)
        if translated:
            stack.title_fa = translated
            stack.save(update_fields=['title_fa'])


class Migration(migrations.Migration):
    dependencies = [
        ('tech_stack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techstack',
            name='title_fa',
            field=models.CharField(blank=True, max_length=100, verbose_name='عنوان فارسی'),
        ),
        migrations.RunPython(populate_persian_titles, migrations.RunPython.noop),
    ]
