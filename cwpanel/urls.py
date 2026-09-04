from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from catalogo.sitemaps import StaticViewSitemap, CategoriaSitemap, ProductoSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'categorias': CategoriaSitemap,
    'productos': ProductoSitemap,
}

urlpatterns = [
    # Django admin nativo oculto en ruta no predecible
    path('sistema/django-interno/', admin.site.urls),

    # Sitemap XML para buscadores
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Robots.txt dinámico
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    # Rutas de la aplicación catálogo
    path('', include('catalogo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
