from django.contrib import admin
from games_critics.models import GamesCritics


# Register your models here.
class GamesAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "slug"]
    list_editable = ["year"]


admin.site.register(GamesCritics, GamesAdmin)