# Generated by Django 4.0.3 on 2022-08-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_paid_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waiting confirmation', 'waiting confirmation'), ('ordered', 'ordered'), ('shipped', 'shipped'), ('received', 'received')], default='ordered', max_length=255),
        ),
    ]
