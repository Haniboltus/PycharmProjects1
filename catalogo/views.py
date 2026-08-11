from django.shortcuts import render, redirect
from .models import Bolo
from .forms import BoloForm

def pagina_inicial(request):
    return render(request, 'catalogo/index.html')

def lista_bolos(request):
    #Busca todos os bolos no banco de dados
    bolos = Bolo.objects.all()
    #Devolve a pagina de listagem de bolos
    #Com o dicionario bolos
    return render(request,
                  'catalogo/lista_bolos.html',
                  {'bolos' : bolos})

def novo_bolo(request):
    if request.method == 'POST':
        form = BoloForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_bolos')
    else:
        form = BoloForm()

    return render(request,
                   'catalogo/bolo_form.html',
                   {'form' : form})
