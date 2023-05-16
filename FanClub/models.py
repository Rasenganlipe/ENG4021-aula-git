from django.db import models #importando o models da db do django



class album (models.Model): #criação da classe album usada na views.py e admin
  nome = models.CharField(max_length = 50)
  ano = models.DateField()
  n_musicas = models.CharField(max_length = 50)
  real = models.BooleanField()

class musica (models.Model): #criação da classe musica usada na views.py e admin
  nome = models.CharField(max_length = 50)
  ano = models.DateField()
  downloads=models.CharField(max_length = 50)
  aplicativo=models.BooleanField()
  