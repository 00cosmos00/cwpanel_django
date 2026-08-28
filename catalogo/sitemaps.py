from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Categoria


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
