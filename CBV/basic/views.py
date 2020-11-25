from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.

class FirstCbv(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "This is template view "
        return context