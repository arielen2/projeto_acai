from django.shortcuts import render, redirect
from .forms import SorveteForm
def sorvete_pedido(request):
    if request.method == 'POST':
        form = SorveteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido') #redireciona para a pasgina de sucesso apos salvar
    else:
        form = SorveteForm()

    return render(request,'main/index.html', {'form': form})