from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pala', 'titulo', 'video_url', 'plataforma', 'fecha')
    list_filter = ('plataforma', 'fecha')
    search_fields = ('titulo', 'pala__nombre', 'video_url')
    ordering = ('pala__nombre', 'titulo')  # Orden alfabético por nombre de pala y título

    fieldsets = (
        (None, {
            'fields': ('pala', 'titulo', 'video_url', 'plataforma')
        }),
    )
    readonly_fields = ('fecha',)
    
    # Mejora la interfaz de selección de la pala
    raw_id_fields = ('pala',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('pala')

admin.site.register(Review, ReviewAdmin)
