from django.db import models

class Numero(models.Model):
    numero_id = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.valor)
