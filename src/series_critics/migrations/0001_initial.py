# Generated by Django 4.0.6 on 2022-08-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=128)),
                ('resume', models.TextField(max_length=2048)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'serie',
                'verbose_name_plural': 'series',
                'ordering': ['-title', 'year'],
            },
        ),
    ]
