# Generated by Django 2.2.11 on 2020-06-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adresse',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
