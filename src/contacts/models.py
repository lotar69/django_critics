from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class Contact(models.Model):
    ROLES = (
        ('Actor', 'Actor'),
        ('Director', 'Director'),
        ('Musician', 'Musican'),
        ('Producer', 'Producer'),
        ('Writer', 'Writer'),
    )

    first_name = models.CharField(max_length=64, verbose_name="Prénom")
    last_name = models.CharField(max_length=64, verbose_name="Nom")
    role = models.CharField(choices=ROLES, max_length=32, verbose_name="Métier")
    nationality = models.CharField(max_length=64, verbose_name="Nationalité")
    birthdate = models.DateField(null=True, verbose_name="Date de Naissance")
    birthplace = models.CharField(max_length=64, null=True, verbose_name="Lieu de naissance")
    photo = models.ImageField(upload_to='uploads/', null=True, verbose_name="Photo")
    like = models.IntegerField(null=True)
    slug = models.SlugField(null=True, blank=True)
    bio = models.TextField(max_length=2048, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Personnalité"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_absolute_url():
        return reverse("contacts:home")

    @property
    def creator_or_default(self):
        return self.creator.username if self.creator else "Createur non renseigné"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)

