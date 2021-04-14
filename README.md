# Búsqueda de datos xml

![dependencies](https://img.shields.io/badge/python-v3.6.9-blue.svg)
![Current Version](https://img.shields.io/badge/version-1.14.15-green.svg)

Esta aplicación se diseñó para leer archivos XML y CSV, abecés el archivo XML es muy grande y se necesita buscar N cantidad de datos que manual mente como humanos nos podemos demora mucho, con esta aplicación nos ahorramos el tiempo de formatear el archivo y buscar esos datos, además también podemos exportar un dato importante a un archivo csv, para usarlo a la necesidad del usuario.

## Tabla de contenido

- [Búsqueda de datos xml](#búsqueda-de-datos-xml)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Instalar Python 3](#instalar-python-3)
    - [Guía de como instalar Python 3 en Linux](#guía-de-como-instalar-python-3-en-linux)
  - [Configuración](#configuración)
    - [Archivos necesarios para trabajar con la aplicación](#archivos-necesarios-para-trabajar-con-la-aplicación)
    - [Como usar la aplicación](#como-usar-la-aplicación)
      - [Comandos de ayuda](#comandos-de-ayuda)
      - [Comando para buscar datos en archivo XML](#comando-para-buscar-datos-en-archivo-xml)
      - [Comando para formatear archivos XML](#comando-para-formatear-archivos-xml)
      - [Comando para exportar los números de estados de cuenta a un archivo CSV](#comando-para-exportar-los-números-de-estados-de-cuenta-a-un-archivo-csv)
      - [Comando para eliminar datos del archivo XML](#comando-para-eliminar-datos-del-archivo-xml)
      - [Comando para elegir días de mora alzar](#comando-para-elegir-días-de-mora-alzar)
    - [Correr aplicación con el archivo de Bash](#correr-aplicación-con-el-archivo-de-bash)
      - [Configurar las variables de entorno](#configurar-las-variables-de-entorno)
      - [Configurar .bashrc_aliases o .zshrc_aliases](#configurar-bashrc_aliases-o-zshrc_aliases)
      - [Ejemplos de como utilizar la aplicación con Bash](#ejemplos-de-como-utilizar-la-aplicación-con-bash)
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

La aplicación al momento de trabajar con el archivo XML buscará la etiqueta `<ESTADOCUENTA>`, que tiene el número de estado de cuenta, que es un dato único que no se repite y con este dato podremos copiar toda la información al archivo nuevo.

**Estructura que debe tener el archivo CSV:**

Números de estados de cuenta |
-----------------------------|
12345 |
67890 |
98765 |
43210 |

>**NOTA:** La aplicación solo lee los números de estados de cuenta, entonces el archivo CSV no debe tener ningún encabezado, si el archivo tiene encabezado o un dato de tipo string o un dato desconocido la aplicación generar un erro porque estará buscando datos o que no existen en el archivo XML o un dato erróneo.
>> Pongo el título **Números de estados de cuenta** para ilustrar como deben ir los datos en el archivo csv, y los datos están delimitados por un salto de línea `\n` para que la aplicación solo se encargue de leer los números.

La aplicación al momento de trabajar con el archivo CSV, buscar en el archivo los números de estados de cuenta que serán buscados en el archivo XML.

**Estructura que debe tener el archivo CSV con los días de mora:**

Números-obligación |Días de mora|
-------------------|------------|
12345 |0
67890 |4
98765 |5
43210 |20

> **NOTA:** la aplicación lee los números de obligación y los días de mora, entonces el archivo CSV no debe tener ningún encabezado, si el archivo tiene encabezado o un dato de tipo string o un dato desconocido la aplicación generar un erro.
>> Pongo el título **Números-obligación** y **Días de mora** para ilustrar como deben ir los datos en el archivo csv, y los datos están delimitados por un puto y coma `;`,`Ejemplo: 12345;0`

 **NOTA:**`En la raíz del proyecto, en la carpeta docs/, habrá archivos CSV, XML y días de mora de ejemplo para testear la aplicación.`

### Como usar la aplicación

Después de clonar este repositorio en su directorio, nos movemos al proyecto ejecuté el siguiente comando:

```shell
cd xml_data_search/
```

> Ya estando en la raíz del proyecto podremos ejecutar los comandos que tiene la aplicación.

#### Comandos de ayuda

La aplicación tiene un comando de ayuda para poder saber como utilizar la aplicación, para ejecutar el comando de ayuda ejecutamos los siguientes comandos:

```shell
python3 main.py -h
o
python3 main.py --help
```

Estos comandos nos mostrar como se puede utilizar la aplicación y que comandos recibe.

#### Comando para buscar datos en archivo XML

Con el siguiente comando podremos exportar a un archivo XML, los datos que necesitemos del archivo XML más grande, a un XML más pequeño y con los datos que el usuario.

Para exportar los datos ejecutamos el siguiente comando:

```shell
python3 main.py file-CSV.csv file-XML.xml name-of-new-XML-file.xml
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = file-CSV.csv ⟵ Archivo CSV con los números de estados de cuenta a buscar.`

`Posición 2 = file-XML.xml ⟵ Archivo XML con la información que se va a copiar.`

`Posición 3 = name-of-new-XML-file ⟵ Nombre del nuevo archivo XML.`

#### Comando para formatear archivos XML

Con el siguiente comando podremos dar formato a los archivos XML.

Abecés los archivos XML Vienen con la información comprimida, entonces a la aplicación le queda muy difícil leer la información comprimida, entonces con este comando podemos dar formato a los archivos xml que necesite leer la información, para formatear un archivo ejecutamos el siguiente comando:

```shell
python3 main.py -f XML-file-to-format.xml
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = -f ⟵ Bandera que indica a la aplicación que se necesita formatear el archivo xml.`

`Posición 2 = XML-file-to-format.xml ⟵ Archivo XML al que se va a formatear.`

#### Comando para exportar los números de estados de cuenta a un archivo CSV

Con el siguiente comando podremos exportar los números de estados de cuenta a un archivo CSV.

Si el usuario los desea puede exportar todos los números de estados de cuenta que estén en el archivo XML a un archivo CSV, para exportarlos ejecutamos el siguiente comando:

```shell
python3 main.py -e XML-file.xml CSV-name.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = -e ⟵ Bandera que indica a la aplicación que se necesita exportar los datos.`

`Posición 2 = XML-file.xml ⟵ Archivo XML donde está la información a exportar.`

`Posición 3 = CSV-name.csv ⟵ Archivo CSV donde se va a exportar la información.`

#### Comando para eliminar datos del archivo XML

Con el siguiente comando podremos eliminar datos del archivo XML.

Si el usuario necesitar eliminar una N cantidad de datos del archivo XML, lo puede hacer utilizando [la misma forma de como se buscan los datos](##comando-para-buscar-datos-en-archivo-xml), pero esta vez la aplicación buscar los estados de cuenta y los eliminará y utilizara una bandera `-r`, para eliminar los datos debemos ejecutar el siguiente comando:

```shell
python3 main.py -r file-CSV.csv file-XML.xml
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = -r ⟵ Bandera que indica a la aplicación que se necesita remover datos.`

`Posición 3 = CSV-name.csv ⟵ Archivo CSV con los números de estados de cuenta que se necesitan eliminar.`

`Posición 2 = XML-file.xml ⟵ Archivo XML donde está la información que se va a eliminar.`

#### Comando para elegir días de mora alzar

Con el siguiente comando podremos elegir días de mora alzar.

Si el usuario desea elegir N días de mora al azar, el sistema tomara un número que indique el usuario y el generar esa cantidad de días de morar y los imprime en consola, lo pude hacer con el siguiente comando:

```shell
python3 main.py -rav file-CSV.csv number-days
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = -rav ⟵ Bandera que indica a la aplicación que se van a generar días de mora al azar.`

`Posición 3 = CSV-name.csv ⟵ Archivo CSV con los días de mora que se van a seleccionar al azar.`

`Posición 2 = number-days ⟵ Se ingresa el número que desear imprimir ejemplo: 5.`

### Correr aplicación con el archivo de Bash

En la raíz del proyecto hay un archivo llamado `script.sh`, con este archivo podremos ejecutar la aplicación sin la necesidad de poner el comando `python3` antes de ejecutar la aplicación, además otras ventajas que tiene de ejecutar la aplicación es que se puede configurar para poder ejecutar la aplicación en cualquier parte del sistema Linux, y seguirá recibiendo los mismos parámetros que recibe si lo estuviera tirando desde el directorio raíz, para configurar esté archivo debemos seguir las siguientes instrucciones:

#### Configurar las variables de entorno

En el directorio raíz hay un archivo llamado `.env-example`, en la terminal debemos hacer lo siguiente, ejecutamos el siguiente comando:

```sh
cat .env-example > .env
```

Con este comando podremos copiar las variables de entorno que tiene la aplicación al archivo `.env`.

Con el nuevo archivo creado procedemos a saber la ruta completa donde se clonó el proyecto y ejecutamos el siguiente comando:

```sh
pwd
```

Sabiendo ya la ruta que imprime la terminal, procedemos a copiar toda la ruta en el archivo `.env` en la parte que dice `PATH_SCRIPT=""`, dentro de esta variable de entorno ponemos la ruta de la aplicación, un ejemplo de como poner la ruta serías así:

```sh
PATH_SCRIPT="/home/USER-linux/ruta-donde-clonó-el-repositorio/xml_data_search/main.py"
```

> Al final de la ruta debemos poner nombre del archivo `main.py` para que él `script.sh` pueda saber como ejecutar la aplicación

Ya con la variable de entorno definida procedemos configurar el `script.sh` para que el sistema lo pueda leer en cualquier parte del sistema.

#### Configurar .bashrc_aliases o .zshrc_aliases

Nos dirigimos al `$HOME` de Linux `~$:` donde están los archivos `.bashrc` o `.zshrc` y con un editor de texto como `vim` o `nano`, nos dirigimos casi al final del archivo, y el archivo debe tener las siguientes líneas de código:

`.bashrc`

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

**En `.zshrc` debes crear estas líneas de código:**

```zsh
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi
```

Ya verificando que están estás línea de código podremos agregar la aplicación en el archivo `.bashrc_aliases` o `.zshrc_aliases`, y lo hacemos de la siguiente manera, agregando estas líneas de código:

```zsh
# Ejecutar la aplicación xml_data_search
alias script-search-xml=". /home/USER-linux/ruta-donde-clonó-el-repositorio/xml_data_search/script.sh"
```

> Al final de la ruta debemos poner el nombre del archivo `script.sh` para poder ejecutar la aplicación por medio de `BASH`, y también recuerda poner un (`.`) antes de la ruta para que se pueda ejecutar, y si no te gusta el punto también puede poner el comando `bash`.

Cuando hayas agregado el alias, debes guardar el archivo y luego ejecutar el siguiente comando para que Linux pueda reconocer la aplicación en el sistema y el comando sería:

```zsh
source .bashrc
o
source .zshrc
```

Si todo sale bien, en la terminal no debe aparecer nada y para verificar que quedo cargada en el sistema podemos ejecutar el siguiente comando:

```zsh
alias | grep script-search-xml
```

Y en la terminal nos mostrará el alias con la ruta del script que agregaste y ya puede ejecutar la aplicación en la terminal, en ejemplo de como saber si quedo bien, podemos ejecutar el siguiente comando:

```zsh
script-search-xml -h
```

Y la aplicación debe imprimir en la terminal las ayudas que tiene la aplicación.

#### Ejemplos de como utilizar la aplicación con Bash

Ya con haber configurado seguido los pasos anteriores, te muestro algunos ejemplos de como utilizar la aplicación por medio del `script.sh` con `Bash` y esto son algunos ejemplos:

```zsh
# Con esté comando imprimes en la terminal la ayudas de la aplicación
script-search-xml -h

# Con esté comando podrás exportar los datos XML a uno nuevo
script-search-xml file-CSV.csv file-XML.xml name-of-new-XML-file.xml

# Con esté comando podrás formatear los archivos XML
script-search-xml -f XML-file-to-form

# Con esté comando podrás exportar los números de estados de cuenta a un archivo CSV
script-search-xml -e XML-file.xml CSV-name.csv

# Con esté comando podrás elegir días de mora alzar
script-search-xml -rav file-CSV.csv number-days
```

## Licencia

>Puede consultar la licencia completa [aquí](https://github.com/steven-ospina/xml_data_search/blob/master/LICENSE)

Este proyecto tiene la licencia de acuerdo con los términos de la licencia del **MIT**.
