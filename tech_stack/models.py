from django.db import models

from portofilo.persian_content import TECH_TRANSLATIONS, translated_value

class TechStack(models.Model):
    title = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100, blank=True, verbose_name='عنوان فارسی')
    percent = models.IntegerField()
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.title

    @property
    def title_fa_display(self):
        return translated_value(self.title_fa, self.title, TECH_TRANSLATIONS)
