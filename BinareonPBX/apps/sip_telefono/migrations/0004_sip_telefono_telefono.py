# Generated by Django 4.1.1 on 2022-09-22 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anexos_sip', '0007_remove_sip_buddies_telefono'),
        ('sip_telefono', '0003_remove_sip_telefono_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='sip_telefono',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono', to='anexos_sip.sip_buddies'),
        ),
    ]
