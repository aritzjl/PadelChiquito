from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Pala, Comentario, Estrella
from django.contrib.auth.decorators import login_required



@login_required
def comentar_pala(request, pala_id):
    if request.method == 'POST':
        usuario = request.user
        pala = get_object_or_404(Pala, pk=pala_id)
        contenido = request.POST.get('contenido')

        if contenido:
            comentario = Comentario(usuario=usuario, pala=pala, contenido=contenido)
            comentario.save()

    return HttpResponseRedirect(reverse('mostrar_pala', args=(pala_id,)))


@login_required
def valorar_pala(request, pala_id):
    if request.method == 'POST':
        usuario = request.user
        pala = get_object_or_404(Pala, pk=pala_id)
        valoracion = request.POST.get('valoracion')

        if valoracion and valoracion.isdigit() and 1 <= int(valoracion) <= 5:
            estrella, created = Estrella.objects.get_or_create(usuario=usuario, pala=pala,valoracion=valoracion)
            estrella.valoracion = int(valoracion)
            estrella.save()

    return HttpResponseRedirect(reverse('mostrar_pala', args=(pala_id,)))