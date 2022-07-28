from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from contacts.models import Contact


# Create your views here.
class ContactHome(ListView):
    model = Contact
    context_object_name = "contacts"


class ContactCreate(CreateView):
    model = Contact
    context_object_name = "contact"
    template_name = "contacts/contact_create.html"
    fields = ["first_name", "last_name", "role", "nationality"]


class ContactDetail(DetailView):
    model = Contact
    context_object_name = "contact"


class ContactUpdate(UpdateView):
    model = Contact
    context_object_name = "contact"
    template_name = "contacts/contact_edit.html"
    fields = ["first_name", "last_name", "role", "nationality",]


class ContactDelete(DeleteView):
    model = Contact
    context_object_name = "contact"
    template_name = "contacts/contact_delete.html"
    success_url = reverse_lazy("contacts:home")