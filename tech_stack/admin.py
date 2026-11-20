from django.contrib import admin
from tech_stack.models import TechStack


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_fa', 'percent')
    search_fields = ('title', 'title_fa')
