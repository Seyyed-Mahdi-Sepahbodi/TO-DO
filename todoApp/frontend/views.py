from django.shortcuts import render
from django.views import View

# Create your views here.

def list_functional_view(request):
    return render(request, 'frontend/list_by_function.html')


class ListClassView(View):
    def get(self, request):
        return render(request, 'frontend/list_by_api_class_view.html')