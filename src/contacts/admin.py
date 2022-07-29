from django.contrib import admin

# Register your models here.
from contacts.models import Contact


class CriticsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "role", "slug"]
    list_editable = ["slug"]


admin.site.register(Contact, CriticsAdmin)
