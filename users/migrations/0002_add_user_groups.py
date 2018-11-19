# Generated by Django 2.1.2 on 2018-11-19 11:57

from django.contrib.auth.models import Group
from django.db import migrations

GROUPS = ["administrator", "secretary", "expert", "planner"]


def add_groups(apps, schema_editor):
    for group in GROUPS:
        group_object, created = Group.objects.get_or_create(name=group)


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [migrations.RunPython(add_groups)]
