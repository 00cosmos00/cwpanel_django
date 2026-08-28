from django.core.management.base import BaseCommand
from catalogo.models import Categoria, Producto


CATEGORIAS = [
    {'nombre': 'Cocinas', 'descripcion': 'Cubiertas, mesones y mobiliario de cocina en maderas nobles seleccionadas.', 'icono': 'fa-utensils', 'orden': 1},
    {'nombre': 'Mesas', 'descripcion': 'Mesas macizas y tableros para comedor, jardín y living.', 'icono': 'fa-table', 'orden': 2},
    {'nombre': 'Oficinas', 'descripcion': 'Escritorios ejecutivos, estanterías y salas de reunión con acabado de lujo.', 'icono': 'fa-briefcase', 'orden': 3},
    {'nombre': 'Revestimientos', 'descripcion': 'Paneles, lamas y tableros finger-joint para muros y arquitectura.', 'icono': 'fa-layer-group', 'orden': 4},
]

PRODUCTOS = [
    # Cocinas
    {
        'nombre': 'Cubierta de Cocina Pino Oregón 32mm',
        'categoria': 'Cocinas',
        'descripcion': 'Tablero alistonado de Pino Oregón grado A, seco en cámara, calibrado y lijado fino grano 150. Ideal para cubiertas de mesón, islas y vanitorios. Disponible en medidas estándar o a pedido.',
        'imagen_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=800&q=80',
        'especies': 'Pino Oregón (Douglas Fir)',
        'espesores': '25mm, 32mm, 40mm',
        'destacado': True, 'activo': True, 'orden': 1,
    },
    {
        'nombre': 'Mesón de Cocina Acacia Negra 40mm',
        'categoria': 'Cocinas',
        'descripcion': 'Tablero macizo de Acacia Negra (Melanoxylon), veta excepcional y dureza superior. Perfecto para cocinas de alta gama y ambientes gastronómicos de autor.',
        'imagen_url': 'https://images.unsplash.com/photo-1556909172-54557c7e4fb7?auto=format&fit=crop&w=800&q=80',
        'especies': 'Acacia Negra (Melanoxylon)',
        'espesores': '32mm, 40mm',
        'destacado': True, 'activo': True, 'orden': 2,
    },
    {
        'nombre': 'Panel de Cocina Roble 18mm',
        'categoria': 'Cocinas',
        'descripcion': 'Panel de Roble Seleccionado para frentes de cajones, puertas de alacenas y revestimiento de islas. Acabado natural UV listo para instalar.',
        'imagen_url': 'https://images.unsplash.com/photo-1556909190-8b67db9fdad0?auto=format&fit=crop&w=800&q=80',
        'especies': 'Roble Seleccionado',
        'espesores': '18mm',
        'destacado': False, 'activo': True, 'orden': 3,
    },
    # Mesas
    {
        'nombre': 'Mesa Comedor Maciza Acacia 40mm',
        'categoria': 'Mesas',
        'descripcion': 'Tablero macizo de Acacia Negra para mesa comedor de 8 personas. Veta natural irrepetible, bordes naturales opcionales. Seco en cámara, estabilidad garantizada.',
        'imagen_url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80',
        'especies': 'Acacia Negra (Melanoxylon)',
        'espesores': '40mm, 50mm',
        'destacado': True, 'activo': True, 'orden': 1,
    },
    {
        'nombre': 'Mesa de Centro Pino Oregón 25mm',
        'categoria': 'Mesas',
        'descripcion': 'Tablero alistonado Pino Oregón para living y terraza. Acabado cera natural o barniz marino para uso exterior. Dimensiones personalizadas.',
        'imagen_url': 'https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?auto=format&fit=crop&w=800&q=80',
        'especies': 'Pino Oregón (Douglas Fir)',
        'espesores': '25mm, 32mm',
        'destacado': False, 'activo': True, 'orden': 2,
    },
    {
        'nombre': 'Mesa de Jardín Eucalipto 32mm',
        'categoria': 'Mesas',
        'descripcion': 'Mesa exterior de Eucalipto Glóbulus, madera de alta densidad y resistencia natural a la humedad. Ideal para terrazas, jardines y áreas de BBQ.',
        'imagen_url': 'https://images.unsplash.com/photo-1530018607912-eff2daa1bac4?auto=format&fit=crop&w=800&q=80',
        'especies': 'Eucalipto Glóbulus',
        'espesores': '32mm, 40mm',
        'destacado': False, 'activo': True, 'orden': 3,
    },
    # Oficinas
    {
        'nombre': 'Escritorio Ejecutivo Roble 25mm',
        'categoria': 'Oficinas',
        'descripcion': 'Tablero para escritorios corporativos de alta gama. Roble Seleccionado, libre de defectos, acabado natural UV. Transmite serenidad y sofisticación en cualquier espacio de trabajo.',
        'imagen_url': 'https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&w=800&q=80',
        'especies': 'Roble Seleccionado',
        'espesores': '25mm, 32mm',
        'destacado': True, 'activo': True, 'orden': 1,
    },
    {
        'nombre': 'Estantería Modular Pino Oregón 18mm',
        'categoria': 'Oficinas',
        'descripcion': 'Tableros calibrados para bibliotecas, estanterías y mobiliario de oficina. Acabado liso grano 150, listo para pintar o barnizar a gusto.',
        'imagen_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80',
        'especies': 'Pino Oregón (Douglas Fir)',
        'espesores': '18mm, 25mm',
        'destacado': False, 'activo': True, 'orden': 2,
    },
    # Revestimientos
    {
        'nombre': 'Lamas Verticales Acacia 18mm',
        'categoria': 'Revestimientos',
        'descripcion': 'Lamas de Acacia para revestimiento de muros interiores y divisiones acústicas. Integración arquitectónica en departamentos y casas de campo. Efecto visual cálido y contemporáneo.',
        'imagen_url': 'https://images.unsplash.com/photo-1538688525198-9b88f6f53126?auto=format&fit=crop&w=800&q=80',
        'especies': 'Acacia Negra',
        'espesores': '18mm',
        'destacado': True, 'activo': True, 'orden': 1,
    },
    {
        'nombre': 'Panel Finger-Joint Pino Oregón 12mm',
        'categoria': 'Revestimientos',
        'descripcion': 'Panel finger-joint de Pino Oregón para revestimiento de cielos, muros y zócalos. Alta estabilidad dimensional, sellador ecológico al agua incluido.',
        'imagen_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=800&q=80',
        'especies': 'Pino Oregón (Douglas Fir)',
        'espesores': '12mm, 18mm',
        'destacado': False, 'activo': True, 'orden': 2,
    },
]


class Command(BaseCommand):
    help = 'Carga datos de ejemplo para categorías y productos de CW Panel'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos de ejemplo...')

        cat_map = {}
        for c in CATEGORIAS:
            obj, created = Categoria.objects.get_or_create(
                nombre=c['nombre'],
                defaults={
                    'descripcion': c['descripcion'],
                    'icono': c['icono'],
                    'orden': c['orden'],
                    'activa': True,
                }
            )
            cat_map[c['nombre']] = obj
            status = 'creada' if created else 'ya existe'
            self.stdout.write(f'  Categoría "{obj.nombre}" — {status}')

        for p in PRODUCTOS:
            cat = cat_map.get(p['categoria'])
            if not cat:
                self.stdout.write(self.style.WARNING(f'  ⚠ Categoría "{p["categoria"]}" no encontrada para "{p["nombre"]}"'))
                continue
            obj, created = Producto.objects.get_or_create(
                nombre=p['nombre'],
                defaults={
                    'categoria': cat,
                    'descripcion': p['descripcion'],
                    'imagen_url': p.get('imagen_url', ''),
                    'especies': p.get('especies', ''),
                    'espesores': p.get('espesores', ''),
                    'destacado': p.get('destacado', False),
                    'activo': p.get('activo', True),
                    'orden': p.get('orden', 0),
                }
            )
            status = 'creado' if created else 'ya existe'
            self.stdout.write(f'  Producto "{obj.nombre}" — {status}')

        self.stdout.write(self.style.SUCCESS('\n✅ Datos de ejemplo cargados correctamente.'))
