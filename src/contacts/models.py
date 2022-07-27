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

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    role = models.CharField(choices=ROLES, max_length=32)
    nationality = models.CharField(max_length=64)
    birthdate = models.DateField(null=True)
    birthplace = models.CharField(max_length=64, null=True)
    photo = models.ImageField(upload_to='uploads/', null=True)
    like = models.IntegerField(null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Person"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_absolute_url():
        return reverse("contacts:home")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)