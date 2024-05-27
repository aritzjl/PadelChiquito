from .models import ContenidoPublicitario


def global_variables(request):
    return {
        'bannerspubli': ContenidoPublicitario.objects.filter(activo=True)[0]
    }