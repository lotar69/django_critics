# Generated by Django 4.0.6 on 2022-08-01 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesCritics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('developper', models.CharField(max_length=128)),
                ('editor', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(choices=[('A', 'Action'), ('R', 'RPG'), ('P', 'Platform'), ('F', 'FPS')], max_length=64)),
                ('resume', models.TextField(max_length=1028)),
                ('score', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=128)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Jeux',
                'ordering': ['-title'],
            },
        ),
    ]
