# 🐍 Anexo VI: Vistas en Django para la aplicación *myOng*

## 1. Introducción

En este tutorial completaremos la primera versión de nuestro sitio web **myOng**, añadiendo **páginas de lista y detalle** para nuestros modelos principales: **Socios** y **Compras**.

El proceso será similar al que usamos al crear la página de inicio. De nuevo, necesitaremos:

* Definir **mapas de URL** (`urls.py`),
* Crear las **vistas** (`views.py`), y
* Diseñar las **plantillas** (`templates/`).

La diferencia principal será que, en las **vistas de detalle**, aprenderemos a extraer información desde los patrones en las URLs y pasarla a la vista. Además, veremos un nuevo tipo de vista: las **vistas genéricas basadas en clases** (*Class-Based Generic Views*).

Estas vistas reducen mucho el código necesario, haciendo nuestras aplicaciones más limpias y fáciles de mantener.

## 2. Tipos de vistas en Django

Django ofrece dos grandes formas de definir vistas:

* **Function-Based Views (FBV)** → funciones de Python que reciben una `HttpRequest` y devuelven una `HttpResponse`.
* **Class-Based Views (CBV)** → clases que heredan de vistas genéricas de Django y proporcionan un modo más estructurado y reutilizable de construir vistas.

### 2.2. Vistas genéricas y el atributo `.model`

Cuando usamos vistas genéricas (por ejemplo, `ListView`, `DetailView`, `CreateView`, etc.), Django necesita saber **qué modelo** debe manejar.
Esto se puede indicar de **dos formas** principales:

#### Forma 1: Declarar explícitamente el modelo con `.model`
##### Ejemplo:

```python
from django.views.generic import ListView
from .models import Socio

class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'
```

##### Qué hace Django automáticamente:

* Crea el **queryset base**: `Socio.objects.all()`.
* Define el **nombre del contexto**: `socio_list` (o `object_list` si no se especifica otro).
* Usa por defecto la plantilla: `socios/socio_list.html` (siguiendo la convención `<app>/<model>_list.html`).

##### Cuándo usarlo:

* Cuando la vista trabaja directamente con un solo modelo.
* Cuando no necesitas modificar el conjunto de datos devuelto.

#### Forma 2: No declarar `.model` y definir `get_queryset()`

Si **no defines** el atributo `.model`, debes indicar manualmente **qué datos** va a mostrar la vista.
Esto se hace sobreescribiendo el método `get_queryset()`.

##### Ejemplo:

```python
from django.views.generic import ListView
from .models import Socio

class SocioListView(ListView):
    template_name = 'socios/socio_list.html'

    def get_queryset(self):
        return Socio.objects.filter(ciudad__nombre='Valdepeñas')
```

##### Qué ocurre aquí:

* Django no sabe qué modelo usar hasta que tú lo indicas.
* Tú tienes control total sobre qué datos se muestran.
* El nombre del contexto por defecto será `object_list`, a menos que definas `context_object_name`.

##### Cuándo usarlo:

* Cuando necesitas filtrar, ordenar o combinar datos de varios modelos.
* Cuando la vista no está asociada directamente a un único modelo.

### 2.3. Comparativa

| Característica        | Con `.model`                                  | Sin `.model`                          |
| --------------------- | --------------------------------------------- | ------------------------------------- |
| Definición del modelo | Se especifica con el atributo `model = Socio` | No se especifica                      |
| Queryset              | Automático (`Socio.objects.all()`)            | Manual (definido en `get_queryset()`) |
| Contexto por defecto  | `<model>_list` o `object_list`                | `object_list`                         |
| Uso recomendado       | Listados o detalles simples                   | Datos filtrados o combinados          |
| Código necesario      | Más simple                                    | Más flexible pero más extenso         |


### 2.4. Ejemplo en el proyecto *myOng*

Supongamos que tienes tu modelo `Socio`:

```python
class Socio(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
```

#### a) Vista sencilla con `.model`:

```python
class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'
```

> Resultado: Muestra todos los socios.

#### b) Vista personalizada sin `.model`:

```python
class SocioListView(ListView):
    template_name = 'socios/socio_list.html'
    context_object_name = 'socios'

    def get_queryset(self):
        return Socio.objects.filter(ciudad='Valdepeñas').order_by('apellidos')
```

> Resultado: Muestra sólo los socios de Valdepeñas, ordenados por apellidos.

## 3. Página de lista de socios

La página de lista mostrará todos los socios registrados en la asociación, con un enlace a su ficha individual (vista de detalle).

📍 URL: `/socios/`
Cada línea mostrará el **nombre completo del socio**, enlazado a su página de detalle.

### 3.1. Mapeo URL

Abre `myong/urls.py` y añade:

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('socios/', views.SocioListView.as_view(), name='socios'),
]
```

Esta función asocia una **ruta** con una **vista** y le da un **nombre** que podremos usar en las plantillas con `{% url 'socios' %}`.



### 3.2. Vista (basada en clases)

Podríamos escribir una vista funcional con `render()`, pero usaremos una **vista genérica**: [`ListView`](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-display/#listview).

Edita `myong/views.py` y añade:

```python
from django.views import generic
from .models import Socio

class SocioListView(generic.ListView):
    model = Socio
```

¡Listo!
Django buscará automáticamente una plantilla llamada
`myong/templates/myong/socio_list.html`.

Dentro de ella, los datos estarán disponibles como `object_list` o `socio_list`.


### 3.3. Opcional: Personalizando la vista

Podemos añadir atributos para modificar el comportamiento por defecto:

```python
class SocioListView(generic.ListView):
    model = Socio
    context_object_name = 'lista_socios'  
    queryset = Socio.objects.filter(pais='España')  
    template_name = 'socios/lista_socios.html'
```

O incluso sobreescribir métodos como `get_queryset()`:

```python
def get_queryset(self):
    return Socio.objects.filter(fecha_alta__year=2024)
```

Y `get_context_data()` para añadir variables adicionales:

```python
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = 'Socios activos'
    return context
```


### 3.4. Creando la plantilla

Crea el archivo:

```
myong/templates/myong/socio_list.html
```

Con el siguiente contenido:

```django
{% extends "base_generic.html" %}

{% block content %}
  <h1>Lista de socios</h1>

  {% if socio_list %}
  <ul>
    {% for socio in socio_list %}
      <li>
        <a href="{{ socio.get_absolute_url }}">{{ socio.nombre }} {{ socio.apellidos }}</a>
      </li>
    {% endfor %}
  </ul>
  {% else %}
    <p>No hay socios registrados.</p>
  {% endif %}
{% endblock %}
```

> En esta plantilla usamos las etiquetas `{% if %}` y `{% for %}`


## 4. Página de detalle de un socio

Esta vista mostrará la **información completa** de un socio:
nombre, apellidos, dirección, país, fecha de alta, etc.

📍 URL: `/socio/<uuid>`

### 4.1. Mapeo URL

Añade a `myong/urls.py`:

```python
path('socio/<uuid:pk>', views.SocioDetailView.as_view(), name='socio-detail'),
```

Aquí usamos `<uuid:pk>` porque todos los identificadores son UUIDs (según la configuración del proyecto).


### 4.2. Vista basada en clases

Edita `myong/views.py` y añade:

```python
class SocioDetailView(generic.DetailView):
    model = Socio
```

Django buscará automáticamente la plantilla:
`myong/templates/myong/socio_detail.html`


### 4.3 Creando la plantilla

Crea el archivo:

```
myong/templates/myong/socio_detail.html
```

Y copia:

```django
{% extends "base_generic.html" %}

{% block content %}
  <h1>{{ socio.nombre }} {{ socio.apellidos }}</h1>

  <p><strong>DNI/NIE:</strong> {{ socio.dni }}</p>
  <p><strong>Fecha de nacimiento:</strong> {{ socio.fecha_nacimiento }}</p>
  <p><strong>Dirección:</strong> {{ socio.direccion }}</p>
  <p><strong>Ciudad:</strong> {{ socio.ciudad }}</p>
  <p><strong>Provincia:</strong> {{ socio.provincia }}</p>
  <p><strong>País:</strong> {{ socio.pais }}</p>
  <p><strong>Fecha de alta:</strong> {{ socio.fecha_alta }}</p>

  {% if socio.iban %}
    <p><strong>IBAN:</strong> {{ socio.iban }}</p>
  {% else %}
    <p><em>Pago mediante transferencia.</em></p>
  {% endif %}
{% endblock %}
```

### 4.4. ¿Y si el socio no existe?

La vista genérica lanza automáticamente un `Http404` si el socio no se encuentra.
Si lo hiciéramos como una vista tradicional:

```python
from django.shortcuts import render, get_object_or_404
from .models import Socio

def socio_detail_view(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    return render(request, 'myong/socio_detail.html', {'socio': socio})
```

## 5. Actualizando la plantilla base

Añade los enlaces en `base_generic.html`:

```django
<li><a href="{% url 'index' %}">Inicio</a></li>
<li><a href="{% url 'socios' %}">Socios</a></li>
<li><a href="#">Compras</a></li>
```

## 6. Tabla de recursos

| Elemento              | Archivo             | Descripción                   |
| --------------------- | ------------------- | ----------------------------- |
| URL lista de socios   | `myong/urls.py`     | `/socios/`                    |
| Vista lista de socios | `SocioListView`     | Lista todos los socios        |
| Plantilla lista       | `socio_list.html`   | Muestra la lista              |
| URL detalle socio     | `myong/urls.py`     | `/socio/<uuid>`               |
| Vista detalle         | `SocioDetailView`   | Muestra los datos de un socio |
| Plantilla detalle     | `socio_detail.html` | Ficha individual del socio    |

## 7. Bibliografía y enlaces a documentación