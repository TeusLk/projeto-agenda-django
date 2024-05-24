from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    last_name = models.CharField(max_length=50, blank=True) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    phone = models.CharField(max_length=50) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    email = models.EmailField(max_length=254, blank=True) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    created_date = models.DateTimeField(default=timezone.now) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    description = models.TextField(blank=True) # Nome da coluna e a config dos valores que vai entrar nessa coluna.
    show = models.BooleanField(default=True) # Se eu quero mostrar o contato.
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # Pra onde vai a imagem enviada... E se é obrigatorio ou não.

    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
