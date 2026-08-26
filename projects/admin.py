from django.contrib import admin
from .models import *

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 2

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'status_percent', 'important', 'is_active')
    list_filter = ('is_active', 'tech_stacks') # اضافه کردن فیلتر بر اساس تکنولوژی
    inlines = [ProjectFeatureInline, ProjectImageInline]
