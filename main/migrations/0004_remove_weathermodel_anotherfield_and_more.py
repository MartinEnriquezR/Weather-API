# Generated by Django 4.1.6 on 2023-02-20 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_weathermodel_anotherfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathermodel',
            name='anotherField',
        ),
        migrations.RemoveField(
            model_name='weathermodel',
            name='newField',
        ),
    ]