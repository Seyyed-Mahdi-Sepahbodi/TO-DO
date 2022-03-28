from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'frontend/home.html'


@login_required
def list_functional_view(request):
    return render(request, 'frontend/list_by_function.html')


class ListClassView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'frontend/list_by_api_class_view.html')