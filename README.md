# Búsqueda de datos xml

![dependencies](https://img.shields.io/badge/python-v3.6.9-blue.svg)
![Current Version](https://img.shields.io/badge/version-1.14.16-green.svg)

Esta aplicación se diseñó para leer archivos XML y CSV, abecés el archivo XML es muy grande y se necesita buscar N cantidad de datos que manual mente como humanos nos podemos demora mucho, con esta aplicación nos ahorramos el tiempo de formatear el archivo y buscar esos datos, además también podemos exportar un dato importante a un archivo csv, para usarlo a la necesidad del usuario.

## Tabla de contenido

- [Búsqueda de datos xml](#búsqueda-de-datos-xml)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Instalar Python 3](#instalar-python-3)
    - [Guía de como instalar Python 3 en Linux](#guía-de-como-instalar-python-3-en-linux)
  - [Configuración](#configuración)
    - [Archivos necesarios para trabajar con la aplicación](#archivos-necesarios-para-trabajar-con-la-aplicación)
    - [Guía de como correr la aplicación con Bash](#guía-de-como-correr-la-aplicación-con-bash)
    - [Como usar la aplicación](#como-usar-la-aplicación)
    - [Listado de Comandos](#listado-de-comandos)
    - [Guía de como funciona la aplicación](#guía-de-como-funciona-la-aplicación)
  - [Licencia](#licencia)

## Instalar Python 3

Para poder ejecutar el proyecto se necesita instalar **Python 3** y es recomendable correr la aplicación en el sistema operativo linux.

### Guía de como instalar Python 3 en Linux

Está guía te indica como instalar **Python 3** en Linux en la distribución `Ubuntu`, si ya tienes instalado **Python 3** `(Recomendable la versión 3.6.9 o superior)`, puedes ignorar esta guía:

[Leer guía de como instalar Python 3 en Ubuntu](docs/guides/install-python-3.md)

## Configuración

Clone esté repositorio con el siguiente comando en la terminal:

```shell
git clone https://github.com/steven-ospina/xml_data_search.git
```

### Archivos necesarios para trabajar con la aplicación

Para poder correr la aplicación, se necesita los archivos CSV y XML para que la aplicación funcione correctamente.

**Estructura que debe tener el archivo XML:**

```xml
<?xml version='1.0' encoding='UTF-8'?>
<root>
  <data>
    <head>
      <id>12345</id>
      <number>556677</number>
      <product>product_1</product>
      <name>pedro</name>
      <reference>00001</reference>
    </head>
  </data>
</root>
```

>**NOTA:** Por lo general el archivo tiene más etiquetas con más datos, pero dejo de ejemplo la etiqueta principal con la que trabaja la aplicación, para entender como funciona la búsqueda de datos.

La aplicación al momento de trabajar con el archivo XML buscará la etiqueta `<id>`, que tiene el número de estado de cuenta, que es un dato único que no se repite y con este dato podremos copiar toda la información al archivo nuevo.

**Estructura que debe tener el archivo CSV:**

ID |
------|
12345 |
67890 |
98765 |
43210 |

>**NOTA:** La aplicación solo lee los id, entonces el archivo CSV no debe tener ningún encabezado, si el archivo tiene encabezado o un dato de tipo string o un dato desconocido la aplicación generar un erro porque estará buscando datos o que no existen en el archivo XML o un dato erróneo.
>> Pongo el título **ID** para ilustrar como deben ir los datos en el archivo csv, y los datos están delimitados por un salto de línea `\n` para que la aplicación solo se encargue de leer los números.

La aplicación al momento de trabajar con el archivo CSV, buscar en el archivo los id que serán buscados en el archivo XML.

**Estructura que debe tener el archivo CSV con las llaves y valores:**

Llaves |Valores|
------|-------|
12345 |0
67890 |4
98765 |5
43210 |20

> **NOTA:** la aplicación lee las llaves y los valores, entonces el archivo CSV no debe tener ningún encabezado, si el archivo tiene encabezado o un dato de tipo string o un dato desconocido la aplicación generar un erro.
>> Pongo el título **Llaves** y **Valores** para ilustrar como deben ir los datos en el archivo csv, y los datos están delimitados por un puto y coma `;`,`Ejemplo: 12345;0`

 **NOTA:**`En la raíz del proyecto, en la carpeta docs/, habrá archivos CSV, XML y llave-valor de ejemplo para testear la aplicación.`

### Guía de como correr la aplicación con Bash

Está guía explica como correr la aplicación con el script de `Bash`:

[Leer guía de como correr la aplicación con Bash](docs/guides/run-application-with-bash.md#correr-aplicación-con-el-archivo-de-bash)

### Como usar la aplicación

Después de clonar este repositorio en su directorio, nos movemos al proyecto ejecuté el siguiente comando:

```shell
cd xml_data_search/
```

> Ya estando en la raíz del proyecto podremos ejecutar los comandos que tiene la aplicación.

### Listado de Comandos

La aplicación tiene disponibles los siguientes comandos:

```zsh
# Con estos comandos imprimes en la terminal las ayudas de la aplicación:
python3 main.py -h
python3 main.py --help
python3 main.py --man
python3 main.py --manual

# Con este comando podrás clonar los datos XML a uno nuevo:
python3 main.py -clone sample-CSV.csv sample-XML.csv name-of-new-XML-file.xml
o
python3 main.py -c sample-CSV.csv sample-XML.csv name-of-new-XML-file.xml

# Con este comando podrás formatear los archivos XML:
python3 main.py -format XML-file-to-format.xml
o
python3 main.py -f XML-file-to-format.xml

# Con este comando podrás exportar múltiples ID a un archivo CSV:
python3 main.py -export sample-XML.xml name-of-new-CSV-file.csv
o
python3 main.py -e sample-XML.xml name-of-new-CSV-file.csv

# Con este comando podrás borrar datos del archivo XML:
python3 main.py -remove sample-CSV.csv sample-XML.xml
o
python3 main.py -r sample-CSV.csv sample-XML.xml

# Con este comando podrás elegir llaves y valores al azar:
python3 main.py -random-access-value sample-key-value.csv (number) <- int
o
python3 main.py -rav sample-key-value.csv (number) <- int

# Con este comando podrás exportar múltiples archivos CSV basado,
# en múltiples archivos XML:
python3 main.py -export-csv PATH-DIRECTORY
o
python3 main.py -ec PATH-DIRECTORY

# Con este comando podrás exportar múltiples archivos XML basado,
# en múltiples datos del archivo CSV, en el directorio,
# que le especifiquen:
python3 main.py -export-xml PATH-DIRECTORY sample-csv.csv
o
python3 main.py -ex PATH-DIRECTORY sample-csv.csv

# Con este comando podrás exportar un solo archivo CSV con múltiples,
# datos de los múltiples datos de los archivos XML en el directorio,
# que le especifiquen:
python3 main.py -export-all PATH-DIRECTORY name-of-new-CSV-file.csv
o
python3 main.py -ea PATH-DIRECTORY name-of-new-CSV-file.csv

# Con este comando podrás unir múltiples archivos CSV en el directorio,
# que le especifiquen y guardara todos los datos que recolecte en un solo,
# archivo CSV:
python3 main.py -merge-csv-files PATH-DIRECTORY name-of-new-CSV-file.csv
o
python3 main.py -mcf PATH-DIRECTORY name-of-new-CSV-file.csv

# Con este comando podrás buscar el ID entre múltiples archivos XML,
# que estén en el directorio que le indiquen y si encuentra el dato,
# mostrar en la terminal la información que encuentre:
python3 main.py -search-data PATH-DIRECTORY DATA-TO_SEARCH
o
python3 main.py -sd PATH-DIRECTORY DATA-TO_SEARCH

# Con este comando podrás comparar dos lista de datos CSV,
# y exportará los datos duplicados a un archivo CSV:
python3 main.py -compare sample-CSV-1.csv sample-CSV-2.csv
o
python3 main.py -C sample-CSV-1.csv sample-CSV-2.csv
```

> **NOTA:** en caso de que quieras saber como funciona cada comando, recomiendo [leer la guía de como funciona la aplicación y cada uno de los comandos.](docs/guides/application-working-guide.md#como-funcionan-los-comandos)

### Guía de como funciona la aplicación

Esta guía te indica a fondo como funciona la aplicación y los comandos disponibles:

[Leer guía de como funciona la aplicación y los comandos](docs/guides/application-working-guide.md#como-funcionan-los-comandos)

## Licencia

>Puede consultar la licencia completa [aquí](https://github.com/steven-ospina/xml_data_search/blob/master/LICENSE)

Este proyecto tiene la licencia de acuerdo con los términos de la licencia del **MIT**.
