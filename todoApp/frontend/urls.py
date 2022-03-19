from django.urls import path

from .views import ListClassView, list_functional_view, HomePageView

app_name = 'frontend'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('function_base/', list_functional_view, name='function_base_list_page'),
    path('class_base/api_view/', ListClassView.as_view(), name='class_base_list_page'),
]
