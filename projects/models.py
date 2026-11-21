from urllib.parse import quote

from django.core.exceptions import ValidationError
from django.db import models

from portofilo.persian_content import (
    CATEGORY_TRANSLATIONS,
    COMMON_TEXT_TRANSLATIONS,
    FEATURE_TRANSLATIONS,
    IMAGE_TRANSLATIONS,
    PROJECT_TRANSLATIONS,
    translated_value,
)
from tech_stack.models import TechStack


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام')
    name_fa = models.CharField(max_length=100, blank=True, verbose_name='نام فارسی')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def name_fa_display(self):
        return translated_value(self.name_fa, self.name, CATEGORY_TRANSLATIONS)


class Project(models.Model):
    TELEGRAM_BOT_USERNAME = 'Younes_web_developer_bot'

    title = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100, blank=True, verbose_name='عنوان فارسی')
    image_default = models.ImageField()
    status_percent = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    status_fa = models.CharField(max_length=100, blank=True, verbose_name='وضعیت فارسی')
    description = models.TextField()
    description_fa = models.TextField(blank=True, verbose_name='توضیحات فارسی')
    important = models.IntegerField(default=1)
    tech_stacks = models.ManyToManyField(TechStack, related_name='projects', blank=True)
    categories = models.ManyToManyField(Category, related_name='projects', verbose_name='دسته‌بندی‌ها')
    github_link = models.URLField(max_length=255, null=True, blank=True)
    live_demo_link = models.URLField(max_length=255, null=True, blank=True)
    cilend_or_role = models.CharField(max_length=100, null=True, blank=True)
    cilend_or_role_fa = models.CharField(max_length=100, null=True, blank=True, verbose_name='نقش یا کارفرما به فارسی')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # ---- فروش پروژه ----
    is_for_sale = models.BooleanField(
        default=False,
        verbose_name='پروژه فروشی است',
        help_text='با فعال کردن این گزینه، پروژه به عنوان پروژه فروشی نمایش داده می‌شود.',
    )
    price = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        verbose_name='قیمت',
        help_text='قیمت پروژه (به تومان). اگر «پروژه فروشی است» فعال باشد، پر کردن این فیلد اجباری است.',
    )
    is_sale_button_active = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='دکمه خرید فعال باشد',
        help_text='اگر غیرفعال باشد، دکمه خرید نمایش داده می‌شود اما قابل کلیک نیست. (وقتی پروژه فروشی است، تعیین این گزینه اجباری است.)',
    )

    def clean(self):
        super().clean()
        errors = {}
        if self.is_for_sale:
            if self.price is None:
                errors['price'] = 'وقتی پروژه فروشی است، وارد کردن قیمت اجباری است.'
            if self.is_sale_button_active is None:
                errors['is_sale_button_active'] = 'وقتی پروژه فروشی است، تعیین وضعیت دکمه خرید اجباری است.'
        if errors:
            raise ValidationError(errors)

    @property
    def price_display(self):
        if self.price is None:
            return ''
        return f'{self.price:,}'

    @property
    def telegram_buy_link(self):
        message = f'من پروژه {self.title} را می‌خوام خریداری کنم'
        return f'https://t.me/{self.TELEGRAM_BOT_USERNAME}?text={quote(message)}'

    def _persian_value(self, field_name, source_value):
        explicit_value = getattr(self, field_name)
        fallback = PROJECT_TRANSLATIONS.get(self.title, {}).get(field_name)
        generic_fallback = COMMON_TEXT_TRANSLATIONS.get(source_value)
        return explicit_value or fallback or generic_fallback or source_value or ''

    @property
    def title_fa_display(self):
        return self._persian_value('title_fa', self.title)

    @property
    def status_fa_display(self):
        return self._persian_value('status_fa', self.status)

    @property
    def description_fa_display(self):
        return self._persian_value('description_fa', self.description)

    @property
    def cilend_or_role_fa_display(self):
        return self._persian_value('cilend_or_role_fa', self.cilend_or_role)

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
    image_name_fa = models.CharField(max_length=255, null=True, blank=True, verbose_name='نام فارسی تصویر')
    number_sort = models.IntegerField(default=0)

    @property
    def image_name_fa_display(self):
        return translated_value(self.image_name_fa, self.image_name, IMAGE_TRANSLATIONS)


class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    feature = models.TextField()
    feature_fa = models.TextField(blank=True, verbose_name='ویژگی به فارسی')

    @property
    def feature_fa_display(self):
        return translated_value(self.feature_fa, self.feature, FEATURE_TRANSLATIONS)
