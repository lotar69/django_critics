from django.shortcuts import render
from django.views.generic import ListView
from contacts.models import Contact
# Create your views here.


class ContactHome(ListView):
    models = Contact
    context_object_name = "contact"

