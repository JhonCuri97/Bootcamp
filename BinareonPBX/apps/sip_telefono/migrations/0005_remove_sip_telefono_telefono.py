# Generated by Django 4.1.1 on 2022-09-22 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sip_telefono', '0004_sip_telefono_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sip_telefono',
            name='telefono',
        ),
    ]
