from django.shortcuts import render, redirect #funções usadas no views.py
from .models import album , musica #classes do models.py que são utilizadas no view.py


def home(request):
    albuns = album.objects.all() #albuns se tornam todos os objetos da classe album
    musicas=musica.objects.all() #musicas se tornam todos os objetos da classe musica
    context = {"albuns": albuns, "musicas":musicas} #define o context
    return render(request, "home.html", context=context) #realiza a request que renderiza home

#Abaixo são definidos separadamente a lista_albuns e a lista_musicas nos HTMLs respectivos
def lista_albuns(request): 
    albuns = album.objects.all()
    context = {"albuns": albuns}
    return render(request, "lista_albuns.html", context=context)
  
def lista_musicas(request):
    musicas = musica.objects.all()
    context = {"musicas": musicas}
    return render(request, "lista_musica.html", context=context)

#Abaixo são definidos separadamente a forms_albuns e a forms_musicas nos HTMLs respectivos
def forms_albuns(request):
    # Se o usuário submeter o formulário, ele cai no if abaixo
    if request.method == "POST":
        if "True" not in request.POST:
            real = False
        else:
            real = True
        album.Objects.create(
                            nome=request.POST["nome"],
                            ano=request.POST["ano"],
                            n_musicas=request.POST["n_musicas"],
                            real=real)
        return redirect("lista_albuns")  #redireciona para lista_albuns

    return render(request, "form_album.html") #redireciona para form_album.html

def forms_musicas(request):
    # Se o usuário submeter o formulário, ele cai no if abaixo
    if request.method == "POST":
        if "True" not in request.POST:
            aplicativo = False
        else:
            aplicativo = True
        musica.objects.create(
                            nome=request.POST["nome"],
                            ano=request.POST["ano"],
                            downloads=request.POST["downloads"],
                            aplicativo=aplicativo)
        return redirect("lista_albuns") #redireciona para lista_albuns

    return render(request, "form_musica.html")  #redireciona para form_musica.html


def update_album(request, album_id): #função para dar update no album
    album = album.objects.get(id=album_id)
    # É necessário converter o objeto datetime para uma string para que ele apareça corretamente como valor do input do meu template
    album.ano = album.ano.strftime('%Y-%m-%d')

    if request.method == "POST":
        album.nome = request.POST["nome"]
        album.ano = request.POST["ano"]
        album.n_musicas = request.POST["n_musicas"]
        if "real" not in request.POST:
            album.real = False
        else:
            album.real = True
        album.save()
        return redirect("lista_album")
    context = { "album":album}
    return render(request, "form_album.html", context=context)#adiciona a album ao form de album


def delete_album(request, album_id): #função para dar delete no album
    album = album.objects.get(id=album_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        album.delete()

      return redirect("lista_album")  #redireciona para lista_album
    context = { "album":album}
    return render(request, "delete_album.html", context=context) #deleta o album

def update_musica(request, musica_id): #função para dar update na musica
    musica = musica.objects.get(id=musica_id)
    # É necessário converter o objeto datetime para uma string para que ele apareça corretamente como valor do input do meu template
    musica.ano = musica.ano.strftime('%Y-%m-%d')

    if request.method == "POST":
        musica.nome = request.POST["nome"]
        musica.ano = request.POST["ano"]
        musica.downloads = request.POST["downloads"]
        if "aplicativo" not in request.POST:
            musica.aplicativo = False
        else:
            musica.aplicativo = True
        musica.save()
        return redirect("lista_musica")
    context = { "musica":musica}
    return render(request, "form_musica.html", context=context) #adiciona a musica ao form de musica


def delete_musica(request, musica_id): #função para dar delete na musica
    musica = musica.objects.get(id=musica_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        musica.delete()

      return redirect("lista_musicas")  #redireciona para lista_musicas.html
    context = { "musica":musica}
    return render(request, "delete_musica.html", context=context) #deleta a musica