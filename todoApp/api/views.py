from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Task, Category
from .serializers import TaskCreateSerializer, TaskListSerializer, CategoryListSerializer

# Create your views here.


# function-base views
# -----------------------------------------------------------------------------
@api_view(['GET'])
def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at')
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    print(request.data)
    serializer = TaskCreateSerializer(data=request.data)

    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update_view(request, pk):
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

# -----------------------------------------------------------------------------


# class-base views based on APIView class
# -----------------------------------------------------------------------------
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


class TaskUpdateDeleteByAPIView(APIView):

    def post(self, request, pk):
        data = request.data
        task = Task.objects.get(id=pk)
        serializer = TaskCreateSerializer(task, data=data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return Response('Item successfully delete!')


class CategoryListByAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)
# -----------------------------------------------------------------------------

# class-base views based on generic api views
# -----------------------------------------------------------------------------
class TaskListCreateByGenericApiViews(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = TaskListSerializer
        else:
            serializer_class = TaskCreateSerializer
        return serializer_class