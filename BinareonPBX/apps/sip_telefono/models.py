from django.db import models

# Create your models here.

class marca_telefono(models.Model):
    id_marca_telefono = models.AutoField(primary_key=True)
    no_marca_telefono = models.CharField(max_length=100, blank=True, null=True,)
    il_activo = models.BooleanField(default=True, blank=True, null=True,)
    il_formato_mac = models.IntegerField(default=0, blank=True, null=True,)
    il_need_mac_for_provisioning = models.BooleanField(default=False, blank=True, null=True,)
    no_extension_for_provisioning = models.CharField(max_length=100, blank=True, null=True,)

    class Meta:
        db_table = "tc_marca"

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    
    def __str__(self):
        return f'{self.id_marca_telefono} / {self.no_marca_telefono} '

class modelo_telefono(models.Model):
    id_modelo_telefono = models.AutoField(primary_key=True)
    no_modelo_telefono = models.CharField(max_length=100, blank=True, null=True,)
    id_marca_telefono = models.ForeignKey(marca_telefono, on_delete=models.CASCADE)
    il_activo = models.BooleanField(default=True, blank=True, null=True,)

    class Meta:
        db_table = "tc_modelo"

        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelo'

    def __str__(self):
        return f'{self.id_modelo_telefono} / {self.no_modelo_telefono} '

class sip_telefono(models.Model):
    id_sip_telefono = models.AutoField(primary_key=True)
    id_usuario_sip = models.CharField(unique=True,max_length=80, blank=True, null=True,)
    id_marca_telefono = models.ForeignKey(marca_telefono, on_delete=models.CASCADE, blank=True, null=True,)
    id_modelo_telefono = models.ForeignKey(modelo_telefono, on_delete=models.CASCADE, blank=True, null=True,)
    no_mac = models.CharField(max_length=100, blank=True, null=True,)
    no_ip_dominio = models.CharField(max_length=50, blank=True, null=True,)
    no_ruta = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        db_table = "tb_sip_telefono"

        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'

    def __str__(self):
        return f'{self.id_sip_telefono} / {self.id_usuario_sip} '