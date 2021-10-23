from django.contrib import admin
from .models import TagCounter


@admin.register(TagCounter)
class TagCounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'status')
