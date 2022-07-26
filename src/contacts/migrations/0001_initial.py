# Generated by Django 4.0.6 on 2022-07-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('role', models.CharField(choices=[('Actor', 'Actor'), ('Director', 'Director'), ('Musician', 'Musican'), ('Producer', 'Producer'), ('Writer', 'Writer')], max_length=32)),
                ('nationality', models.CharField(max_length=64)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=64)),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('like', models.IntegerField()),
            ],
        ),
    ]