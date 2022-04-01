from django.urls import path

from .views import (TaskListCreateViewByAPIView, TaskUpdateDeleteByAPIView,
                    task_create_view, task_delete_view, task_list_view,
                    task_update_view, CategoryListByAPIView)

app_name = 'api'
urlpatterns = [
     path('function_base/list/', task_list_view, name='function_task_list'),
     path('function_base/create/', task_create_view, name='function_task_create'),
     path('function_base/update/<int:pk>/',
         task_update_view, name='function_task_update'),
     path('function_base/delete/<int:pk>/',
         task_delete_view, name='function_task_delete'),

     path('class_base/apiview/list_create/',
         TaskListCreateViewByAPIView.as_view(), name='class_task_list_apiview'),
     path('class_base/apiview/update_delete/<int:pk>/',
         TaskUpdateDeleteByAPIView.as_view(), name='class_task_update_delete_apiview'),
     path('class_base/apiview/category/list/', CategoryListByAPIView.as_view(), name='category_list'),

]
