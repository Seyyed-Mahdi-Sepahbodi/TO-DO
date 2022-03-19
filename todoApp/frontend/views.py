from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'frontend/home.html'


def list_functional_view(request):
    return render(request, 'frontend/list_by_function.html')


class ListClassView(View):
    def get(self, request):
        return render(request, 'frontend/list_by_api_class_view.html')