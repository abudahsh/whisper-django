from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView


class RegisterView(TemplateView):
    template_name = 'register.html'