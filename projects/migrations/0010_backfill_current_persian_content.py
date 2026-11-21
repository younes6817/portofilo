from django.db import migrations

from portofilo.persian_content import (
    CATEGORY_TRANSLATIONS,
    FEATURE_TRANSLATIONS,
    IMAGE_TRANSLATIONS,
    PROJECT_TRANSLATIONS,
    TECH_TRANSLATIONS,
)


def fill_blank_persian_fields(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    ProjectFeature = apps.get_model('projects', 'ProjectFeature')
    ProjectImage = apps.get_model('projects', 'ProjectImage')
    Category = apps.get_model('projects', 'Category')
    TechStack = apps.get_model('tech_stack', 'TechStack')

    for project in Project.objects.all():
        translations = PROJECT_TRANSLATIONS.get(project.title, {})
        changed_fields = []
        for field_name, translated_text in translations.items():
            if not getattr(project, field_name):
                setattr(project, field_name, translated_text)
                changed_fields.append(field_name)
        if changed_fields:
            project.save(update_fields=changed_fields)

    for model, source_field, target_field, translations in (
        (ProjectFeature, 'feature', 'feature_fa', FEATURE_TRANSLATIONS),
        (ProjectImage, 'image_name', 'image_name_fa', IMAGE_TRANSLATIONS),
        (Category, 'name', 'name_fa', CATEGORY_TRANSLATIONS),
        (TechStack, 'title', 'title_fa', TECH_TRANSLATIONS),
    ):
        for item in model.objects.all():
            source_text = getattr(item, source_field)
            translated_text = translations.get(source_text)
            if translated_text and not getattr(item, target_field):
                setattr(item, target_field, translated_text)
                item.save(update_fields=[target_field])


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0009_persian_content_fields'),
    ]

    operations = [
        migrations.RunPython(fill_blank_persian_fields, migrations.RunPython.noop),
    ]
