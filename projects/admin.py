from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa')
    search_fields = ('name', 'name_fa')

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('type', 'image', 'image_name', 'image_name_fa', 'number_sort')

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 2
    fields = ('feature', 'feature_fa')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'status_percent', 'important', 'is_active', 'is_for_sale')
    list_filter = ('is_active', 'is_for_sale', 'tech_stacks', 'categories')
    inlines = [ProjectFeatureInline, ProjectImageInline]
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'description', 'image_default', 'status', 'status_percent', 'important', 'is_active', 'tech_stacks', 'categories'),
        }),
        ('محتوای فارسی', {
            'fields': ('title_fa', 'description_fa', 'status_fa', 'cilend_or_role_fa'),
            'description': 'این متن‌ها هنگام انتخاب زبان فارسی در سایت نمایش داده می‌شوند.',
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('cilend_or_role', 'start_date', 'end_date', 'github_link', 'live_demo_link'),
        }),
        ('فروش پروژه', {
            'fields': ('is_for_sale', 'price', 'is_sale_button_active'),
            'description': 'اگر گزینه «پروژه فروشی است» را فعال کنید، پر کردن «قیمت» و تعیین وضعیت «دکمه خرید» اجباری می‌شود.',
        }),
    )
