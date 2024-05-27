from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone', 'show') # Lista do que aparecer no campo de ADM do Django
    ordering = ('-id',) # Ordena a pelo o que vc quer a tabela 
   # list_filter = ('created_date', ) # pode filtrar por | HOJE | 7 DIAS | 1 MES | 1 ANO
    search_fields = ('id','first_name', 'last_name', 'phone') # Barra de pesquisa para pesquisar 
    list_per_page = 10 # Quantas linhas eu quero na tabela
    list_max_show_all = 100 # Maximo de linhas que eu quero na tabela 
    list_editable = ('first_name', 'last_name', 'show' ) # Edita o valor direto na tabela
    list_display_links = ('id',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', # Lista do que aparecer no campo de ADM do Django
    ordering = '-id', # Ordena a pelo o que vc quer a tabela 
   
