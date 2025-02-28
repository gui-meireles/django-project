from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    # Caso adicione um - antes do data_fotografia, ele inverte o order_by
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if 'buscar' in request.GET:
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
        # O 'buscar' abaixo faz referência a tag 'name' que está no input de pesquisa do index.html
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})