# Configurar el archivo configXML.yaml

En la raíz del proyecto se debe crear el archivo llamado `configXML.yaml`, con este archivo la aplicación pude entender como están conformadas la estructura del archivo XML que se vaya a trabajar, no es necesario que crees el archivo manual mente, la aplicación tiene un método llamado `yaml_configuration` que está en el archivo`Config.py`, para crear el archivo y con sus valores que tiene por defecto, debemos ejecutar el comando:

```shell
python3 main.py -h
o
python3 main.py --help
```

Con el comando anterior imprime en la terminal la ayudas que tiene la aplicación, pero cuando `Python` empieza a verificar toda la aplicación, ejecutara el método `yaml_configuration` y esté método verifica que el archivo esté en el directorio raíz del proyecto, como no lo va a encontrar, él creara el archivo y con sus valores que tiene definidos por defectos.

## Tabla de contenido

- [Configurar el archivo configXML.yaml](#configurar-el-archivo-configxmlyaml)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Estructura que tiene el archivo configXML.yaml](#estructura-que-tiene-el-archivo-configxmlyaml)
    - [PRODUCT_PATH](#product_path)
    - [ROOT_XML](#root_xml)
    - [SEARCH_PARAMETERS](#search_parameters)
    - [TAG_TO_SEARCH](#tag_to_search)
    - [TITLE_KEY_VALUE](#title_key_value)
    - [XML_DOM_PATH](#xml_dom_path)
    - [RUN](#run)

## Estructura que tiene el archivo configXML.yaml

El archivo tiene la siguiente estructura:

```yaml
DEV:
  PRODUCT_PATH: ./data/head/product
  ROOT_XML: root
  SEARCH_PARAMETERS:
  - id
  - number
  - product
  - reference
  - name
  TAG_TO_SEARCH: id
  TITLE_KEY_VALUE: KEY | VALUE
  XML_DOM_PATH: ./data/head
PROD:
  PRODUCT_PATH: ''
  ROOT_XML: ''
  SEARCH_PARAMETERS: []
  TAG_TO_SEARCH: ''
  TITLE_KEY_VALUE: ''
  XML_DOM_PATH: ''
RUN:
  MODE: DEV
```

> **NOTA:** El archivo se diseñó con estas propiedades con el fin de poder leer archivos XML sin la necesidad de tener una estructura definida en el código y pueda ser más dinámico a la hora de leer los archivos XML.

A continuación explico para qué sirve cada una de las propiedades, las configuraciones están basa en el [archivo XML de ejemplo](../../docs/sample-XML.xml) que está en la carpeta `doc/` en el directorio del proyecto.

Las rutas del archivo XML están definidas con la forma que trabaja la librería `xml.etree.ElementTree`

### PRODUCT_PATH

La propiedad `PRODUCT_PATH` hace referencia a la etiqueta XML que tiene el [archivo XML de ejemplo](../../docs/sample-XML.xml), en el ejemplo hago referencia a la ruta `./data/head/product`, pero para entender te muestro como está conformado en el archivo XML:

```xml
<data>
    <head>
        <product>product_1</product>
    </head>
</data>
```

La aplicación en caso de buscar una etiqueta `<product></product>` pero con la etiqueta padre del `<head></head>`, que este caso es `<data></data>`, lo buscará con la ruta `./data/head/product`.

Ejemplo de como definir las rutas:

```yaml
PRODUCT_PATH: ./data/head/product
# Otra forma de definir la ruta sería:
PRODUCT_PATH: .//product
```

### ROOT_XML

La propiedad `ROOT_XML` hace referencia a la etiqueta XML que tiene el [archivo XML de ejemplo](../../docs/sample-XML.xml), en el ejemplo hago referencia a la ruta `root`, pero para entender te muestro como está conformado en el archivo XML:

```xml
<root>
</root>
```

La aplicación en caso de buscar la etiqueta `<root></root>`, lo buscará con la ruta `root`, la etiqueta **root** es la etiqueta padre que contiene todos los datos del archivo XML.

Ejemplo de como definir las rutas:

```yaml
ROOT_XML: root
# Otra forma de definir la ruta sería con un puto:
ROOT_XML: .
```

### SEARCH_PARAMETERS

La propiedad `SEARCH_PARAMETERS` almacena una lista **(Array)** de propiedades que hacen referencia a las etiquetas que tendría el [archivo XML de ejemplo](../../docs/sample-XML.xml) y serian las siguientes etiquetas de ejemplo:

```xml
<head>
    <id>12345</id>
    <number>556677</number>
    <product>product_1</product>
    <reference>00001</reference>
    <name>pedro</name>
</head>
```

Para que la aplicación pueda buscar estas etiquetas y su contenido debemos agregarlo en el archivo `configXML.yaml` de la siguiente manera:

```yaml
# Definiendo los parámetros como una lista:
SEARCH_PARAMETERS:
- id
- number
- product
- reference
- name

# Otra forma seria como un array de datos:
SEARCH_PARAMETERS: [id, number, product, reference, name]
```

### TAG_TO_SEARCH

La propiedad `TAG_TO_SEARCH` hace referencia a la etiqueta XML que tiene el [archivo XML de ejemplo](../../docs/sample-XML.xml), en el ejemplo hago referencia a la ruta `id`, pero para entender te muestro como está conformado en el archivo XML:

```xml
<id> </id>
```

La aplicación en caso de buscar una etiqueta `<id></id>`, lo buscará con la ruta `id`, la utilizo para solo buscar está etiqueta, es seria un dato único y que no se deberá repetir en ninguno de los datos.

Ejemplo de como definir la ruta:

```yaml
TAG_TO_SEARCH: id
```

**Pero en el caso de que queramos buscar un dato en específico en los archivos XML, podemos cambiar con otra etiqueta, como ejemplo `number`, `reference`, `name`.**

> **NOTA:** Si se necesita buscar un dato que no sea un `id` que es único, ten en cuenta que la etiqueta que definas y el dato que vas a buscar debe ser único, si el dato no es único, la aplicación buscara entre N cantidad de archivos XML y el primer dato que encuentre, este será el que se mostrará en la terminal.

Para entender para qué se utiliza esta propiedad, recomiendo leer él [comandó para buscar datos entre multiples archivos XML](application-working-guide.md#comando-para-buscar-datos-entre-multiples-archivos-xml), que está en el archivo `application-working-guide.md`.

### TITLE_KEY_VALUE

La propiedad `TITLE_KEY_VALUE` es la única propiedad que no se utiliza para trabajar con los archivos XML, esta propiedad solo se utiliza en la clase `Csv.py`, que está ubicado en el directorio raíz del proyecto en la ruta `app/Csc/Csv.py`, el método se llama `select_keys_and_random_values` y solo se utiliza para poner el título de los datos seleccionados aleatoriamente, es solo texto, si lo quieres modificar, solo es cambiar el valor que viene por defecto.

Ejemplo de como definir el título:

```yaml
TITLE_KEY_VALUE: KEY | VALUE
```

### XML_DOM_PATH

La propiedad `XML_DOM_PATH` es la propiedad más importante para leer los archivos XML, con esta propiedad la librería `xml.etree.ElementTree`, tiene un método llamado `findall`, con este método es capas de leer todos los datos que estén en el archivo XML, pero definiendo una ruta en común que debe tener el archivo XML, como ejemplo en el [archivo XML que se diseñó para probar](../../docs/sample-XML.xml), encontraras que todos tiene la siguiente estructura en común:

```xml
<data>
    <head>

    </head>
</data>
```

Todos los datos están guardados en la etiqueta padre del `<head></head>`, pero en la propiedad del archivo `configXML.yaml` defino la ruta `./data/head`, porque con esta ruta la aplicación tiene la facilidad de leer todos los datos del archivo XML.

Ejemplo de como definir las rutas:

```yaml
XML_DOM_PATH: ./data/head
# Otra forma de definir la ruta sería:
XML_DOM_PATH: .//head
```

> **NOTA:** En caso de que necesites leer un archivo XML con una estructura diferente, solo debe comparar como esta la estructura del archivo XML de pruebas y definir las rutas en las propiedades que están en el archivo `configXML.yaml`.
>
> Solo debes tener en cuenta que debes definir bien las rutas del archivo XML que quieras trabajar y tener en cuenta la propiedad [**ROOT_XML**](#root_xml) es la que reconoce la etiqueta principal del archivo XML.

### RUN

La propiedad `RUN` tiene definida la propiedad `MODE` y esta propiedad recibe el valor de `DEV`**(development)** y `PROD`**(production)**, y si te fijas son los modos en que están definidos en el archivo `configXML.yaml`, el modo `DEV` tiene definidos unos parámetros por defecto, pero solo son de muestra para entender como la aplicación lee los archivos XML, y el modo `PROD` están vacíos para que puedas definir las rutas que necesites trabajar con otro archivo XML.

En el caso de que quieras cambiar el modo, solo debes definir en la propiedad `MODE`, cuál será el modo que quieres que la aplicación lea y que propiedades va a tener, puede ser los modos `DEV` o `PROD`, pero si quieres otro modo, lo puedes crear, pero debes tener en cuenta que las propiedades deben ser iguales a los modos `DEV` o `PROD`.

> **NOTA:** Recuerda definir bien el nombre del **MODE** para que la aplicación pueda trabajar correctamente.
