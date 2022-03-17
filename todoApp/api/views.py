from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TaskListSerializer, TaskCreateSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def task_list_view(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    print("createeeeeee")
    print(request.data)
    serializer = TaskCreateSerializer(data=request.data)

    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['POST'])
def task_update_view(request, pk):
    print("updateeeeee")
    task = Task.objects.get(id=pk)
    serializer = TaskCreateSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete_view(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item successfully delete!')


class TaskListCreateViewByAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
