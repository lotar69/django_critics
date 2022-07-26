from django.db import models


# Create your models here.
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
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='uploads/')
    like = models.IntegerField()

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Person"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
