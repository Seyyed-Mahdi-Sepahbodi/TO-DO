from rest_framework import serializers
from .models import Task, Category


class TaskListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', required=False)

    class Meta:
        model = Task
        fields = ['title', 'category', 'priority', 'completed']


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        print(validated_data['title'])
        task = Task(title=validated_data['title'])
        task.save()
        print(task)
        return task