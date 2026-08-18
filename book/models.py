from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return self.title
        