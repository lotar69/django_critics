from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from series_critics.models import Series


# Create your views here.
class SeriesHome(ListView):
    model = Series
    context_object_name = "series"


class SeriesCreate(CreateView):
    model = Series
    context_object_name = "serie"
    template_name = "series_critics/series_create.html"
    fields = ["title", "year", "country", "resume"]


class SeriesDetail(DetailView):
    model = Series
    context_object_name = "serie"
    template_name = "series_critics/series_detail.html"


class SeriesEdit(UpdateView):
    model = Series
    context_object_name = "serie"
    template_name = "series_critics/series_edit.html"
    fields = ["title", "year", "country", "resume"]


class SeriesDelete(DeleteView):
    model = Series
    context_object_name = "serie"
    template_name = "series_critics/series_delete.html"
    success_url = reverse_lazy("series:home")