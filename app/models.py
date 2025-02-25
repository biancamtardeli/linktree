from django.db import models
from django.core.exceptions import ValidationError

class Link(models.Model):
    texto = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return self.texto
    
class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to="perfil", null=True, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"

    def save(self, *args, **kwargs):
        if Perfil.objects.exists() and not self.pk:
            raise ValidationError("Já existe um perfil cadastrado! Você não pode adicionar outro.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
class Icone(models.Model):
    icone = models.CharField(max_length=50)
    texto = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Ícone"
        verbose_name_plural = "Ícones"

    def __str__(self):
        return self.texto
    
class RedeSocial(models.Model):
    url = models.URLField()
    icone = models.ForeignKey(Icone, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"

    def __str__(self):
        return self.icone.texto