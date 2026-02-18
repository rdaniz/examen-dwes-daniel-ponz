# 🐍 Anexo I: Entornos Virtuales en Python

## 1. Entornos Virtuales en Python

En las aplicaciones basadas en Python es frecuente utilizar paquetes y módulos que no forman parte de la librería estándar. Muchas veces, determinadas aplicaciones necesitan de versiones concretas de librerías específicas, y esto implica que la instalación local de Python puede no llegar a cumplir las especificaciones de todas las aplicaciones. 

La solución a este problema son los **entornos virtuales**: se trata de un árbol “autónomo” de directorios que contiene una instalación de Python, para una determinada versión y con una serie de paquetes adicionales.

De esta forma, diferentes aplicaciones pueden utilizar diferentes entornos virtuales, dependiendo de la versión, tanto de Python, como de los paquetes adicionales para que la aplicación funcione correctamente.

### 1.1. Creación de un entorno virtual

El módulo utilizado para la creación de entornos virtuales es **venv**.
Para instalarlo en Linux, el comando es:

```bash
sudo apt install python3-venv 
```

El comando para crear un entorno virtual en un directorio determinado es:

```bash
python3 -m venv app-env
```

Este comando creará el directorio `app-env` con un árbol de directorios que contienen el intérprete de Python y archivos de soporte.
El parámetro `-m` indica al intérprete de Python que se va a ejecutar un módulo, en este caso `venv`, como un script.

> Si quieres saber más sobre los módulos en Python, aquí tienes más información.



Para activar el entorno virtual de Python, se utilizará uno de los siguientes comandos, dependiendo del sistema operativo (desde la ruta en la que se encuentre la carpeta `app-env`):

**En Linux o MacOS:**

```bash
source app-env/bin/activate
```

Tras ejecutar este comando, sabremos que estamos utilizando el entorno virtual porque la línea de comandos pasará a tener el nombre del entorno virtual entre paréntesis:

```bash
(app-env) usuario:$
```

La herramienta `venv` permite crear entornos virtuales aislados para proyectos Python, pero tiene varias limitaciones. Primero, *no gestiona automáticamente las versiones de las dependencias* ni ofrece un sistema para bloquearlas, lo que puede generar incompatibilidades al instalar paquetes en diferentes entornos. Tampoco facilita la actualización o desinstalación ordenada de librerías ni registra los paquetes instalados salvo que se use manualmente un archivo `requirements.txt`. Además, no incluye funciones para publicar proyectos ni manejar metadatos del paquete. 

Por estos problemas, `venv` es útil para aislar entornos, pero requiere otras herramientas como `pip` o `Poetry` para una gestión completa de dependencias.

### 1.2. Gestión de paquetes mediante Poetry

`Poetry` es una **herramienta más completa**: combina la gestión de entornos virtuales **y** la gestión de dependencias y publicación de paquetes.

Se pueden instalar, actualizar o eliminar paquetes utilizando el programa **Poetry**, que gestiona tanto los entornos virtuales como las dependencias del proyecto. Poetry descarga los paquetes, por defecto, del índice de Paquetes de Python [PyPI](https://pypi.org), que puede explorarse manualmente desde un navegador web.

Además, al contrario que con  `venv`, con `Poetry` no es necesario usar `requirements.txt` que se actualice de manera manual cuando se realicen instalaciones, ya que las dependencias se registran automáticamente en el archivo `pyproject.toml` y sus versiones exactas se bloquean en `poetry.lock`.

`Poetry` dispone de una serie de comandos (`add`, `update`, `remove`, `install`, etc.) que pueden consultarse en la [documentación oficial](https://python-poetry.org/docs/).

### 1.3. Instalación de paquetes

Instalar la última versión de un paquete:

```bash
$ poetry add flask
```

Instalar una versión específica:

```bash
$ poetry add requests@2.6.0
```

Actualizar un paquete existente:

```bash
$ poetry update requests
```

Eliminar un paquete:

```bash
$ poetry remove <nombre_paquete>
```

Mostrar información del entorno o dependencias:

```bash
$ poetry show
```

Listar todos los paquetes instalados (con sus dependencias):

```bash
$ poetry show --tree
```

Instalar todas las dependencias del proyecto (según `pyproject.toml` y `poetry.lock`):

```bash
$ poetry install
```

## 2. Creación del primer proyecto Django: MyONG

Vamos a crear nuestro primer proyecto con Django. Para ello, deberemos tener una carpeta de trabajo (puede ser la carpeta de un proyecto que tengamos ya iniciado en github ;-)) o podemos crearla mendiante comandos Linux:

```bash
mkdir MyOng
cd MyOng
```

Una vez localizados en ella, inicializaremos `Poetry` para gestionar las dependencias:
```bash
poetry init
```

Si no hubieramos instalado `Poetry` usamos `apt` de la forma habitual:
```bash
apt install python3-poetry
```

Creamos el primer proyecto Django:

```bash
django-admin startproject MyONG_proyect
```

Aquí también puede darse el caso de no tener descargada esta librería, por lo que usaremos las herramientas de `poetry` para añadirla a nuestro proyecto:

```bash
poetry add django
```

Al hacerlo, se crea una carpeta `myone_proyect` con la estructura base del proyecto:

![Directory Tree](/images/dwes/ejercicios/django-tree.png)

La herramienta crea una nueva carpeta y la llena con archivos para las diferentes partes de la aplicación (como se muestra en la imágen anterior). La mayoría de los archivos están nombrados según su propósito (por ejemplo, las vistas deben almacenarse en **views.py**, los modelos en **models.py**, las pruebas en **tests.py**, la configuración del sitio de administración en **admin.py**, el registro de la aplicación en **apps.py**) y contienen un código mínimo estándar para trabajar con los objetos asociados.

Estudiemos para que sirve cada uno:
* ****init**.py** es un archivo vacío que le indica a Python que trate este directorio como un paquete de Python.
* **settings.py** contiene todas las configuraciones del sitio web, incluyendo el registro de cualquier aplicación que creemos, la ubicación de nuestros archivos estáticos, detalles de configuración de la base de datos, etc.
* **urls.py** define los mapeos URL-a-vista del sitio. Aunque podría contener todo el código de mapeo de URL, es más común delegar parte de los mapeos a aplicaciones particulares, como verás más adelante.
* **wsgi.py** se usa para ayudar a tu aplicación Django a comunicarse con el servidor web. Puedes tratarlo como código estándar.
* **asgi.py** es un estándar para que las aplicaciones y servidores web asincrónicos de Python se comuniquen entre sí. ASGI es el sucesor asincrónico de WSGI. ASGI proporciona un estándar tanto para aplicaciones asincrónicas como sincrónicas de Python, mientras que WSGI solo lo hacía para las sincrónicas. ASGI es compatible hacia atrás con WSGI y soporta múltiples servidores y frameworks de aplicaciones.

Además, ahora tenemos:

* Una carpeta **migrations**, usada para almacenar “migraciones”, archivos que permiten actualizar automáticamente tu base de datos a medida que modificas tus modelos.
* ****init**.py**, un archivo vacío creado para que Django/Python reconozca la carpeta como un paquete de Python y permita usar sus objetos en otras partes del proyecto.

::: note
¿Has notado lo que falta en la lista de archivos anterior? Aunque hay un lugar para tus vistas y modelos, no hay ninguno para tus mapeos de URL, plantillas o archivos estáticos. Te mostraremos cómo crearlos más adelante (no se necesitan en todos los sitios web, pero sí en este ejemplo).
:::

Ahora podemos probar a lanzar la aplicación, ejecutando el siguiente comando desde el directorio principal de nuestra aplicación:

```bash
python manage.py runserver
```

El servidor se lanza por defecto en el **puerto 8000**, y al acceder desde el navegador veremos la página de bienvenida de Django.

### 2.1. Generación de la app Socios

::: note 
Un sitio web puede consistir en una o más secciones. Por ejemplo, sitio principal, blog, wiki, área de descargas, etc. Django te anima a desarrollar estos componentes como aplicaciones separadas, que luego podrían reutilizarse en diferentes proyectos si lo deseas.
:::

A continuación, vamos a crear y registrar la app que incluirá toda la funcionalidad necesaria para manejar a los distintos socios y sus necesidades.

En `Django` el script `manage.py` que se encuentra en la carpeta raíz, es el encargado de realizar parte de estas tareas. Veamos cómo:

1. Generamos la nueva aplicación del proyecto:

```bash
python manage.py startapp socios
```

2. Registra las nuevas aplicaciones para incluirlas en el proyecto y que `Django` la tenga en cuenta cuando se ejecuten las herramientas (como agregar modelos a la base de datos, por ejemplo). Las aplicaciones se registran agregándolas a la lista **INSTALLED_APPS** en la configuración del proyecto.

Abre, utilizando el IDE, el archivo de configuración del proyecto, `myong_proyect/myong_proyect/settings.py`, y encuentra la definición de la lista **INSTALLED_APPS**. Luego añade una nueva línea al final de la lista, como se muestra a continuación:

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Añade nuestra nueva aplicación
    'socios', 
]
```
La nueva línea especifica el objeto de configuración de la aplicación `socios` que se generó automáticamente cuando creaste la aplicación.

::: note
Verás que ya hay muchas otras **INSTALLED_APPS** (y **MIDDLEWARE**, más abajo en el archivo de configuración). Estas habilitan soporte para el sitio de administración de Django y su funcionalidad (incluyendo sesiones, autenticación, etc.).
:::

### 2.2. Otras configuraciones del proyecto

El archivo **settings.py** también se usa para configurar otros ajustes, pero en este punto probablemente solo quieras cambiar **TIME_ZONE**, que debe igualarse a una cadena de la lista estándar de zonas horarias (la columna TZ de la tabla contiene los valores que necesitas). Cambia tu valor de **TIME_ZONE** por uno apropiado para tu zona, por ejemplo:

```python
TIME_ZONE = 'Europe/London'
```

Hay otros dos ajustes que no cambiarás ahora, pero que deberías conocer:

* **SECRET_KEY**: es una clave secreta usada como parte de la estrategia de seguridad de Django. Si no proteges este código en desarrollo, deberás usar otro (quizás leído desde una variable de entorno o archivo) cuando lo pongas en producción.
* **DEBUG**: activa los registros de depuración en caso de error, en lugar de respuestas con código de estado HTTP. Debe establecerse en **False** en producción, ya que la información de depuración puede ser útil para atacantes, pero por ahora podemos dejarlo en **True**.

### 2.3. Probando el marco del sitio web

En este punto, tenemos un proyecto esqueleto completo. El sitio web aún no hace nada, pero vale la pena ejecutarlo para asegurarnos de que ninguno de nuestros cambios ha roto nada.

Antes de hacerlo, primero debemos ejecutar una **migración de base de datos**.
Esto actualiza nuestra base de datos (para incluir cualquier modelo en nuestras aplicaciones instaladas) y elimina algunas advertencias de compilación.


### 2.4. Ejecutando migraciones de base de datos

Django usa un **Object-Relational-Mapper (ORM)** para mapear las definiciones de los modelos en el código Django a la estructura de datos utilizada por la base de datos subyacente.
A medida que cambiamos las definiciones de nuestros modelos, Django rastrea los cambios y puede crear scripts de migración de base de datos para migrar automáticamente la estructura de datos subyacente en la base de datos y hacerla coincidir con el modelo.

Cuando creamos el sitio web, Django añadió automáticamente varios modelos para uso de la sección de administración del sitio (que veremos más adelante).

Ejecuta los siguientes comandos para definir tablas para esos modelos en la base de datos (asegúrate de estar en el directorio que contiene **manage.py**):

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

::: warning
Deberás ejecutar estos comandos cada vez que tus modelos cambien de una forma que afecte la estructura de los datos que deben almacenarse (incluyendo tanto la adición como la eliminación de modelos o campos individuales).
:::

El comando **makemigrations** crea (pero no aplica) las migraciones para todas las aplicaciones instaladas en tu proyecto. Además, puedes especificar el nombre de la aplicación para ejecutar la migración solo para una app. Esto te da la oportunidad de revisar el código de las migraciones antes de aplicarlas.
Si eres un experto en Django, ¡puedes incluso ajustarlas ligeramente!

El comando **migrate** aplica las migraciones a tu base de datos. Django lleva un seguimiento de cuáles han sido añadidas a la base de datos actual.

::: note
Debes volver a ejecutar las migraciones y probar el sitio cada vez que hagas cambios significativos. ¡No lleva mucho tiempo!
:::


