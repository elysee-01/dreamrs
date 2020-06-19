# Generated by Django 2.2.11 on 2020-06-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('fab fa-facebook-f', 'Facebook'), ('fab fa-twitter', 'Twitter'), ('fas fa-globe', 'Globe'), ('fab fa-behance', 'Behance')], max_length=20),
        ),
    ]