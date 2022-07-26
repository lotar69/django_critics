from django.urls import path
from contacts.views import ContactHome


urlpatterns = [
    path("", ContactHome.as_view(), name="create")
]