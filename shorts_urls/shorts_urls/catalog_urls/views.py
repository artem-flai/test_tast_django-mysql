from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, get_user
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegUsers, InOutLink
from .models import Catalog_Urls


def random_literals():
    import random

    literals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shorts_str = ''
    while len(shorts_str) < 6:
        num_lit = random.randrange(0, 10000) % 62
        shorts_str += literals[num_lit]
    return shorts_str


class Reg(CreateView):
    form_class = RegUsers
    template_name = 'catalog_urls/registrations.html'
    success_url = reverse_lazy('log_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистраия'
        return context


class LogIn(LoginView):
    form_class = AuthenticationForm
    template_name = 'catalog_urls/login.html'
    success_url = reverse_lazy('log_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('create_shorts_url')


def create_shorts_url(request):
    short_link = ''
    short_liter = 'A'
    if request.method == "POST":
        create_link__form = InOutLink(request.POST)
        if create_link__form.is_valid():
            data_save = create_link__form.cleaned_data
            short_liter = random_literals()
            short_link = f"http://127.0.0.1:8000/short_u/{short_liter}/"
            data_save['short_link'] = short_liter
            data_save['id_user'] = get_user(request)
            Catalog_Urls.objects.create(**data_save)
    else:
        create_link__form = InOutLink(request.POST)
    return render(request, 'catalog_urls/create_short_url.html', {'form': create_link__form, 'short_link': short_link,
                                                                  'url_s': short_liter})


def catalog_urls(request):
    all_links = Catalog_Urls.objects.all()
    return render(request, 'catalog_urls/catalog.html', {"all_links": all_links})


def short_u(request, url_s):
    all_links = Catalog_Urls.objects.all()
    short_get = ...
    for short in all_links:
        if short.short_link == url_s:
            short_get = short
            return redirect(short.long_link)
    return redirect('catalog_urls', {"all_shorts": all_links, "short_get": short_get})


def logout_user(request):
    logout(request)
    return redirect('log_in')
