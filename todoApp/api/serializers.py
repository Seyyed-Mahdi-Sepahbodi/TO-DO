from rest_framework import serializers
from .models import Task, Category


class TaskListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'priority', 'completed']


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data):
        task = Task(title=validated_data['title'])
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


# class TaskUpdateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Task
#         fields = ['title']

