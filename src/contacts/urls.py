from django.urls import path
from contacts.views import ContactHome, ContactCreate, ContactDetail, ContactUpdate, ContactDelete

app_name = "contacts"

urlpatterns = [
    path("", ContactHome.as_view(), name="home"),
    path("create/", ContactCreate.as_view(), name="create"),
    path("<str:slug>/", ContactDetail.as_view(), name="detail"),
    path("edit/<str:slug>/", ContactUpdate.as_view(), name="update"),
    path("delete/<str:slug>/", ContactDelete.as_view(), name="delete"),
]
