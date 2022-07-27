from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from contacts.models import Contact


# Create your views here.
class ContactHome(ListView):
    model = Contact
    context_object_name = "contacts"


class ContactCreate(CreateView):
    model = Contact
    context_object_name = "contacts"
    template_name = "contacts/contact_create.html"
    fields = ["first_name", "last_name", "role", "nationality"]


class ContactDetail(DetailView):
    model = Contact
    context_object_name = "contacts"


class ContactUpdate(UpdateView):
    model = Contact
    context_object_name = "contacts"
    template_name = "contacts/contact_edit"
    fields = ["first_name", "last_name", "role", "nationality", "birthdate", "birthplace", "photo", "like"]


class ContactDelete(DeleteView):
    model = Contact
    context_object_name = "contacts"