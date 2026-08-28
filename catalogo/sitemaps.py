from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Categoria, Producto


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # Nombres de las urls estáticas principales
        return ['index', 'productos']

    def location(self, item):
        return reverse(item)


class CategoriaSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        # Retorna solo las categorías activas
        return Categoria.objects.filter(activa=True)


class ProductoSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        # Retorna solo los productos activos
        return Producto.objects.filter(activo=True)
