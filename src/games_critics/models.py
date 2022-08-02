import django.contrib.auth.backends
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class GamesCritics(models.Model):
    GENRES = (
        ("A", "Action"),
        ("R", "RPG"),
        ("P", "Platform"),
        ("F", "FPS"),
    )

    title = models.CharField(max_length=128, unique=True)
    developper = models.CharField(max_length=128)
    editor = models.CharField(max_length=128)
    year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(choices=GENRES, max_length=64)
    resume = models.TextField(max_length=1028)
    score = models.IntegerField()
    slug = models.SlugField(max_length=128, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["-title"]
        verbose_name_plural = "Jeux"
        verbose_name = "Jeu"

    @staticmethod
    def get_absolute_url():
        return reverse("games:home")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
            self.save()
        super().save(*args, **kwargs)
