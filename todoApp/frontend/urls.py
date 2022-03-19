from django.urls import path

from .views import ListClassView, list_functional_view

urlpatterns = [
    path('function_base/', list_functional_view, name='function_base_list_page'),
    path('class_base/api_view/', ListClassView.as_view(), name='class_base_list_page'),
]
