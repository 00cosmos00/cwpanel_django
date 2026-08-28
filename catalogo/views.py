from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm


# ─────────────────────────────────────────────
#  VISTAS PÚBLICAS
# ─────────────────────────────────────────────

def index(request):
    """Página principal — fiel al diseño HTML de referencia."""
    productos_destacados = Producto.objects.filter(activo=True, destacado=True).select_related('categoria')[:6]
    categorias = Categoria.objects.filter(activa=True)
    return render(request, 'index.html', {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
    })


def productos_view(request):
    """Página de productos agrupados por categoría."""
    cat_id = request.GET.get('cat')
    categorias = Categoria.objects.filter(activa=True).prefetch_related(
        'productos'
    )

    # Filtrar por categoría si se pasa parámetro
    if cat_id:
        categorias = categorias.filter(pk=cat_id)

    # Solo categorías con productos activos
    categorias_con_productos = []
    for cat in categorias:
        prods = cat.productos.filter(activo=True)
        if prods.exists():
            categorias_con_productos.append((cat, prods))

    todas_categorias = Categoria.objects.filter(activa=True)

    return render(request, 'productos.html', {
        'categorias_con_productos': categorias_con_productos,
        'todas_categorias': todas_categorias,
        'cat_activa': int(cat_id) if cat_id and cat_id.isdigit() else None,
    })


def producto_detalle(request, pk):
    """Página de detalle del producto."""
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    # Productos relacionados de la misma categoría (excluyendo el actual)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True
    ).exclude(pk=pk)[:3]
    
    return render(request, 'producto_detalle.html', {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
    })


# ─────────────────────────────────────────────
#  PANEL ADMIN PERSONALIZADO
# ─────────────────────────────────────────────

def panel_dashboard(request):
    """Dashboard principal del panel admin."""
    ctx = {
        'total_categorias': Categoria.objects.count(),
        'total_productos': Producto.objects.count(),
        'productos_activos': Producto.objects.filter(activo=True).count(),
        'productos_destacados': Producto.objects.filter(destacado=True).count(),
        'ultimos_productos': Producto.objects.order_by('-creado_en')[:5],
    }
    return render(request, 'admin_custom/dashboard.html', ctx)


# ── Categorías ──

def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'admin_custom/categorias_list.html', {'categorias': categorias})


def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('categorias_list')
    return render(request, 'admin_custom/categorias_form.html', {'form': form, 'titulo': 'Nueva Categoría'})


def categoria_edit(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoría actualizada.')
        return redirect('categorias_list')
    return render(request, 'admin_custom/categorias_form.html', {'form': form, 'titulo': f'Editar: {obj.nombre}', 'obj': obj})


def categoria_delete(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Categoría eliminada.')
        return redirect('categorias_list')
    return render(request, 'admin_custom/confirm_delete.html', {'obj': obj, 'tipo': 'Categoría'})


# ── Productos ──

def productos_list(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'admin_custom/productos_list.html', {'productos': productos})


def producto_create(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('productos_list')
    return render(request, 'admin_custom/productos_form.html', {'form': form, 'titulo': 'Nuevo Producto'})


def producto_edit(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto actualizado.')
        return redirect('productos_list')
    return render(request, 'admin_custom/productos_form.html', {'form': form, 'titulo': f'Editar: {obj.nombre}', 'obj': obj})


def producto_delete(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('productos_list')
    return render(request, 'admin_custom/confirm_delete.html', {'obj': obj, 'tipo': 'Producto'})
