from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


# Create your models here.
class Series(models.Model):

    GENRES = (
        ("T", "Thriller"),
        ("A", "Action"),
        ("R", "Romance"),
        ("C", "Comedy")
    )

    PLATFORMS = (
        ("N", "Netflix"),
        ("D", "Disney +"),
        ("P", "Prime Video"),
        ("A", "Apple TV +"),
        ("O", "OCS"),
    )

    years = range(1990, 2022)

    YEARS = [(i, i) for i in years]

    title = models.CharField(max_length=256)
    year = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=128)
    resume = models.TextField(max_length=2048)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-title", "year"]
        verbose_name = "serie"
        verbose_name_plural = "series"

    @staticmethod
    def get_absolute_url():
        return reverse("games:home")