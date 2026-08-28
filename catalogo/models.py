from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=120, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    icono = models.CharField(
        max_length=80, default='fa-box',
        help_text='Clase Font Awesome, ej: fa-tree',
        verbose_name='Ícono FA'
    )
    orden = models.PositiveIntegerField(default=0, verbose_name='Orden')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f"{reverse('productos')}?cat={self.pk}"


class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE,
        related_name='productos', verbose_name='Categoría'
    )
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(
        upload_to='productos/', blank=True, null=True,
        verbose_name='Imagen'
    )
    imagen_url = models.URLField(
        blank=True,
        help_text='URL de imagen externa (Unsplash, etc.) si no se sube archivo',
        verbose_name='URL de imagen externa'
    )
    precio = models.DecimalField(
        max_digits=12, decimal_places=0,
        blank=True, null=True,
        help_text='Precio referencial en CLP (opcional)',
        verbose_name='Precio (CLP)'
    )
    especies = models.CharField(
        max_length=250, blank=True,
        help_text='Ej: Pino Oregón, Acacia',
        verbose_name='Especies de madera'
    )
    espesores = models.CharField(
        max_length=200, blank=True,
        help_text='Ej: 18mm, 25mm, 32mm',
        verbose_name='Espesores disponibles'
    )
    destacado = models.BooleanField(default=False, verbose_name='Destacado')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    orden = models.PositiveIntegerField(default=0, verbose_name='Orden')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.nombre} ({self.categoria})'

    def get_imagen_url(self):
        """Devuelve la URL de imagen a mostrar (subida o externa)."""
        if self.imagen:
            return self.imagen.url
        if self.imagen_url:
            return self.imagen_url
        return None
