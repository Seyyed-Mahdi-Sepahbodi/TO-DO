from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TaskListSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def task_list_view(request):
    tasks = Task.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


class TaskListViewByAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)




