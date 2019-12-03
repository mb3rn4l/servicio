from django.db import models


class Person(models.Model):
    """
        Abstración del usuario
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Apellido')
    address = models.CharField(max_length=100, blank=False, null=False, verbose_name='Dirección')
    city = models.CharField(max_length=50, blank=False, null=False, verbose_name='Ciudad')
    latitud = models.DecimalField(max_digits=15, decimal_places=10, verbose_name="Latitud", blank=True, null=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=10, verbose_name="Longitud", blank=True, null=True)
    estate_geo = models.CharField(max_length=1, blank=True, null=True, default='I', verbose_name='estado geografico')

    class Meta:
        managed = True
        db_table = 'person'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

