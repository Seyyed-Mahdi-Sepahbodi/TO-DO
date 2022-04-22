from django.contrib import admin
from .models import Task, Category

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'priority', 'completed']
    list_editable = ['priority', 'completed', 'category', 'description']

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
