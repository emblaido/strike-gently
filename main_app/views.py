from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponse 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Journal
from .models import Therapy
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

class Therapy(TemplateView):
    template_name = "therapy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["therapy"] = Therapy.objects.all() 
        return context


class JournalList(TemplateView):
    template_name = "journal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["journal"] = Journal.objects.filter(name__icontains=name)
        else:
            context["journal"] = Journal.objects.all()
            context["header"] = "journal"
        return context

class JournalCreate(CreateView):
    model = Journal
    fields = ['name', 'img', 'bio',]
    template_name = "journal_create.html"
    def get_success_url(self):
        return reverse('journal_detail', kwargs={'pk': self.object.pk})

class JournalDetail(DetailView):
    model = Journal
    template_name = "journal_detail.html"

class JournalUpdate(UpdateView):
    model = Journal
    fields = ['name', 'img', 'bio',]
    template_name = "journal_update.html"
    success_url = "/journal/"
    def get_success_url(self):
        return reverse('journal_detail', kwargs={'pk': self.object.pk})

class JournalDelete(DeleteView):
    model = Journal
    template_name = "journal_delete_confirmation.html"
    success_url = "/journal/"
