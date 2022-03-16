from rest_framework import serializers
from .models import Task, Category


class TaskListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Task
        fields = ['title', 'category', 'priority', 'completed']