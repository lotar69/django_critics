from django.urls import path, reverse

from games_critics.views import GameHome, GameCreate, GameDetail, GameDelete, GameUpdate

app_name = "games"

urlpatterns = [
    path("", GameHome.as_view(), name="home"),
    path("create/", GameCreate.as_view(), name="create"),
    path("edit/<str:slug>/", GameUpdate.as_view(), name="edit"),
    path("delete/<str:slug>/", GameDelete.as_view(), name="delete"),
    path("<str:slug>/", GameDetail.as_view(), name="detail"),
]