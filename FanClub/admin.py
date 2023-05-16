from django.contrib import admin #importando o admin para usar no jango (relacionado ao super user)
from .models import album, musica #importando as classes album e musica de models.py(relacionado ao super user)

admin.site.register(album) #registando no site do admin album
admin.site.register(musica) #registando no site do admin musica