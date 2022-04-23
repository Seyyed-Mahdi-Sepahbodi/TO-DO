from rest_framework import serializers
from .models import Task, Category

class TaskListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'priority', 'completed']

    def get_category(self, instance):
        if instance.category:
            return instance.category.title
        return None

class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    priority = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        task = Task(title=validated_data['title'])
        task.save()
        return task

    def update(self, instance, validated_data):
        category = Category.objects.get(title=validated_data.get('category', instance.category))

        instance.title = validated_data.get('title', instance.title)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.description = validated_data.get('description', instance.description)
        instance.category = category
        instance.priority = validated_data.get('priority', instance.priority)
        
        instance.save()
        return instance


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title']
