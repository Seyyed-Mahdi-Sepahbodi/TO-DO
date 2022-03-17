from django.urls import path
from .views import task_list_view, TaskListViewByAPIView, task_create_view, TaskCreateByAPIView

urlpatterns = [
    path('function_base/list/', task_list_view, name='function_task_list'),
    path('class_base/apiview/list/', TaskListViewByAPIView.as_view(), name='class_task_list_apiview'),

    path('function_base/create/', task_create_view, name='function_task_create'),
    path('class_base/apiview/create/', TaskCreateByAPIView.as_view(), name='class_task_create_apiview'),
]