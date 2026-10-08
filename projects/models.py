from urllib.parse import quote

from django.core.exceptions import ValidationError
from django.db import models

from tech_stack.models import TechStack


class Project(models.Model):
    TELEGRAM_BOT_USERNAME = 'Younes_web_developer_bot'

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
