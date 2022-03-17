from django.urls import path
from .views import task_list_view, TaskListCreateViewByAPIView, task_create_view, task_update_view

urlpatterns = [
    path('function_base/list/', task_list_view, name='function_task_list'),
    path('class_base/apiview/list_create/', TaskListCreateViewByAPIView.as_view(), name='class_task_list_apiview'),
    path('function_base/create/', task_create_view, name='function_task_create'),
    path('function_base/update/<int:pk>/', task_update_view, name='function_task_update'),
]