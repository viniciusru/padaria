from django.db import models

class usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=100)
    Pedido = models.IntegerField()
