from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView


class FrontendTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
