from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Públicas
    path('', views.index, name='index'),
    path('productos/', views.productos_view, name='productos'),
    path('productos/<int:pk>/', views.producto_detalle, name='producto_detalle'),

    # Login / Logout del panel
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin_custom/login.html'), name='login'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='logout'),

    # Panel admin personalizado — protegido con @login_required
    path('admin/', views.panel_dashboard, name='panel_dashboard'),

    # Categorías
    path('admin/categorias/', views.categorias_list, name='categorias_list'),
    path('admin/categorias/nueva/', views.categoria_create, name='categoria_create'),
    path('admin/categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),
    path('admin/categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),

    # Productos
    path('admin/productos/', views.productos_list, name='productos_list'),
    path('admin/productos/nuevo/', views.producto_create, name='producto_create'),
    path('admin/productos/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    path('admin/productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]
