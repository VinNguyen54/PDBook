# Generated by Django 4.0.3 on 2022-10-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]