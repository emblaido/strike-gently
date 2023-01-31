from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponse 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class ArtList(TemplateView):
    template_name = "Art_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["art"] = Art.objects.filter(name__icontains=name)
        else:
            context["art"] = Art.objects.all()
            context["header"] = "Art"
        return context

class ArtCreate(CreateView):
    model = Art
    fields = ['name', 'img', 'bio',]
    template_name = "art_create.html"
    def get_success_url(self):
        return reverse('art_detail', kwargs={'pk': self.object.pk})

class ArtDetail(DetailView):
    model = Art
    template_name = "art_detail.html"

class ArtUpdate(UpdateView):
    model = Art
    fields = ['name', 'img', 'bio',]
    template_name = "art_update.html"
    success_url = "/art/"
    def get_success_url(self):
        return reverse('art_detail', kwargs={'pk': self.object.pk})

class ArtDelete(DeleteView):
    model = Art
    template_name = "art_delete_confirmation.html"
    success_url = "/art/"
