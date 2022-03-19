from django.urls import path
from .views import list_functional_view, ListClassView

urlpatterns = [
    path('function_base/', list_functional_view, name='function_base_list_page'),
    path('class_base/api_view/', ListClassView.as_view(), name='class_base_list_page'),
]
