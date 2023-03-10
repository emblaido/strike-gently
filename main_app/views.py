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


class TherapyList(TemplateView):
    template_name = "therapy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["therapy"] = Therapy.objects.all()
        return context


class TherapyDetail(DetailView):
    model = Therapy
    template_name = "therapy_detail.html"


@method_decorator(login_required, name='dispatch')
class JournalList(TemplateView):
    template_name = "journal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print('user')
        print(self.request.user)
        if user != None:
            context["journal"] = Journal.objects.all()
            context['cur_user'] = user
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journals"] = Journal.objects.all()
        print(Journal.objects.all)
        context = super().get_context_data(**kwargs)
        return context


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
            return redirect("therapy")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
