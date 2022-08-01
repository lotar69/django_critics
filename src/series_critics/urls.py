from django.urls import path

from series_critics.views import SeriesHome, SeriesCreate, SeriesDetail, SeriesEdit, SeriesDelete

app_name = "series"

urlpatterns = [
    path("", SeriesHome.as_view(), name="home"),
    path("create/", SeriesCreate.as_view(), name="create"),
    path("<str:slug>/", SeriesDetail.as_view(), name="detail"),
    path("edit/<str:slug>/", SeriesEdit.as_view(), name="edit"),
    path("delete/<str:slug>/", SeriesDelete.as_view(), name="delete")
]
