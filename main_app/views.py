from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

class Art:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

class ArtList(TemplateView):
    template_name = "Art_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Art"] = Art
        return context
