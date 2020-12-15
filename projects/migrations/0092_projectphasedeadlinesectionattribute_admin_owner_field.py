# Generated by Django 2.2.13 on 2020-12-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0091_conditional_minimum_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectphasedeadlinesectionattribute',
            name='admin_field',
            field=models.BooleanField(default=False, verbose_name='show for administrator'),
        ),
        migrations.AddField(
            model_name='projectphasedeadlinesectionattribute',
            name='owner_field',
            field=models.BooleanField(default=False, verbose_name='show for project owner'),
        ),
    ]
