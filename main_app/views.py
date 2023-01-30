from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Art
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

        art = [
  Art("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
          "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),]
 

class ArtList(TemplateView):
    template_name = "Art_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["art"] = Art.objects.filter(name__icontains=name)
        else:
            context["art"] = Art.objects.all()
            context["header"] = "Art Therapy"
        return context
