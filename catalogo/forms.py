from django import forms
from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'icono', 'orden', 'activa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cocinas'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve de la categoría'}),
            'icono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: fa-utensils'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'categoria', 'descripcion',
            'imagen', 'imagen_url',
            'precio', 'especies', 'espesores',
            'destacado', 'activo', 'orden'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio en CLP (opcional)'}),
            'especies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pino Oregón, Acacia'}),
            'espesores': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 18mm, 25mm, 32mm'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
            'destacado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
