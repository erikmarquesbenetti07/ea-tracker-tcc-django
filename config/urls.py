from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("usuarios.urls")),
    path("gestor/", include("gestores.urls")),
    path("cliente/", include("clientes.urls")),
    path("associado/", include("associados.urls")),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
