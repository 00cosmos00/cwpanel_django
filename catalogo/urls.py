from django.urls import path
from . import views

urlpatterns = [
    # Públicas
    path('', views.index, name='index'),
    path('productos/', views.productos_view, name='productos'),
    path('productos/<int:pk>/', views.producto_detalle, name='producto_detalle'),

    # Panel admin personalizado
    path('panel/', views.panel_dashboard, name='panel_dashboard'),

    # Categorías
    path('panel/categorias/', views.categorias_list, name='categorias_list'),
    path('panel/categorias/nueva/', views.categoria_create, name='categoria_create'),
    path('panel/categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),
    path('panel/categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),

    # Productos
    path('panel/productos/', views.productos_list, name='productos_list'),
    path('panel/productos/nuevo/', views.producto_create, name='producto_create'),
    path('panel/productos/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    path('panel/productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]
