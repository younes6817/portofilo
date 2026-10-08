from django.contrib import admin
from .models import *

admin.site.register(Category)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 2

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'status_percent', 'important', 'is_active', 'is_for_sale')
    list_filter = ('is_active', 'is_for_sale', 'tech_stacks', 'categories')
    inlines = [ProjectFeatureInline, ProjectImageInline]
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'description', 'image_default', 'status', 'status_percent', 'important', 'is_active', 'tech_stacks', 'categories'),
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('cilend_or_role', 'start_date', 'end_date', 'github_link', 'live_demo_link'),
        }),
        ('فروش پروژه', {
            'fields': ('is_for_sale', 'price', 'is_sale_button_active'),
            'description': 'اگر گزینه «پروژه فروشی است» را فعال کنید، پر کردن «قیمت» و تعیین وضعیت «دکمه خرید» اجباری می‌شود.',
        }),
    )
