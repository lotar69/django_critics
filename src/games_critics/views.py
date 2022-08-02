from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from games_critics.models import GamesCritics


class GameHome(ListView):
    model = GamesCritics
    template_name = "games_critics/games_list.html"
    context_object_name = "games"


class GameCreate(CreateView):
    model = GamesCritics
    template_name = "games_critics/games_create.html"
    context_object_name = "game"
    fields = ["title", "developper", "editor", "year", "score"]


class GameDetail(DetailView):
    model = GamesCritics
    template_name = "games_critics/games_detail.html"
    context_object_name = "game"


class GameUpdate(UpdateView):
    model = GamesCritics
    template_name = "games_critics/games_update.html"
    context_object_name = "game"
    fields = ["title", "year"]


class GameDelete(DeleteView):
    model = GamesCritics
    template_name = "games_critics/games_delete.html"
    context_object_name = "game"
    success_url = reverse_lazy("games:home")