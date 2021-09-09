from django.contrib import admin
from frutos.models import Familia, Pessoa, Reuniao, Frequencia

class Familias(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Familia, Familias)

class Pessoas(admin.ModelAdmin):
    list_display = ('id','nome','familia','data_nascimento', 'sexo')
    list_display_links = ('id','nome')
    search_fields = ['familia__nome','nome','sexo',]
    # search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Pessoa, Pessoas)

class Reunioes(admin.ModelAdmin):
    list_display = ('id', 'data_reuniao','tipo')
    list_display_links = ('id',)
    search_fields = ('data_reuniao',)
    list_per_page = 20

admin.site.register(Reuniao, Reunioes)

class Frequencias(admin.ModelAdmin):
    list_display = ('id', 'pessoa','reuniao')
    list_display_links = ('id',)

admin.site.register(Frequencia, Frequencias)
