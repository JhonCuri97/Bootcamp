from django.db import models

# Create your models here.
class sip(models.Model):
    idbuzon = models.IntegerField(primary_key=True)
    customer_id = models.CharField(unique=True, max_length=25)
    context = models.CharField(max_length=50, blank=True, null=True)
    mailbox = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=50, blank=True, null=True)
    attach = models.CharField(max_length=4, blank=True, null=True)
    saycid = models.CharField(max_length=4, blank=True, null=True)
    hidefromdir = models.CharField(max_length=4, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "buzon_voz"
"""
class nuevo_sip(models.Model):
    id_buzon_voz = models.AutoField(primary_key=True)
    customer_id = models.CharField(unique=True, max_length=25)
    context = models.CharField(max_length=50, blank=True, null=True)
    mailbox = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=50, blank=True, null=True)
    attach = models.CharField(max_length=4, blank=True, null=True)
    saycid = models.CharField(max_length=4, blank=True, null=True)
    hidefromdir = models.CharField(max_length=4, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
"""
