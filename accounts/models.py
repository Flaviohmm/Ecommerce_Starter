from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=200, verbose_name="Rua")
    number = models.CharField(max_length=20, verbose_name="Número")
    complement = models.CharField(max_length=100, blank=True, verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    state = models.CharField(max_length=2, verbose_name="UF")
    zip_code = models.CharField(max_length=9, verbose_name="CEP")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}"
    
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
