# Generated by Django 4.1.1 on 2022-09-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sip_telefono', '0001_initial'),
        ('anexos_sip', '0002_alter_sip_buddies_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sip_buddies',
            name='telefono',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono', to='sip_telefono.sip_telefono'),
        ),
    ]
