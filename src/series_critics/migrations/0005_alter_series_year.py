# Generated by Django 4.0.6 on 2022-07-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series_critics', '0004_alter_series_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
