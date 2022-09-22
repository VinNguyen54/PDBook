# Generated by Django 4.0.3 on 2022-09-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_note_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
