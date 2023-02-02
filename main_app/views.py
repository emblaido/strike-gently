from contextlib import _RedirectStream
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponse 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Journal
from .models import Therapy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

class Therapy(TemplateView):
    template_name = "therapy.html"

@method_decorator(login_required, name='dispatch')
class JournalList(TemplateView):
    template_name = "journal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["journal"] = Journal.objects.filter(name__icontains=name)
        else:
            Journal.objects.filter(user=self.request.user)
            context["journal"] = Journal.objects.all()
            context["header"] = "journal"
        return context

class JournalCreate(CreateView):
    model = Journal
    fields = ['name', 'img', 'bio',]
    template_name = "journal_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JournalCreate, self).form_valid(form)
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

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("journal")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

