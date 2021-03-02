# Búsqueda de datos xml

![dependencies](https://img.shields.io/badge/python-v3.6.9-blue.svg)
![Current Version](https://img.shields.io/badge/version-1.9.5-green.svg)

Esta aplicación se diseñó para leer archivos XML y CSV, abecés el archivo XML es muy grande y se necesita buscar N cantidad de datos que manual mente como humanos nos podemos demora mucho, con esta aplicación nos ahorramos el tiempo de formatear el archivo y buscar esos datos, además también podemos exportar un dato importante a un archivo csv, para usarlo a la necesidad del usuario.

## Tabla de contenido

- [Búsqueda de datos xml](#búsqueda-de-datos-xml)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Instalar python 3](#instalar-python-3)
    - [Procedemos a instalar python3 en la distribución de linux Ubuntu](#procedemos-a-instalar-python3-en-la-distribución-de-linux-ubuntu)
      - [1 - Actualizamos las dependencias y paquetes del sistema](#1---actualizamos-las-dependencias-y-paquetes-del-sistema)
      - [2 - Comprobamos la versión del Python 3](#2---comprobamos-la-versión-del-python-3)
      - [2 - Instalamos Python 3 en el sistema](#2---instalamos-python-3-en-el-sistema)
  - [Dependencias](#dependencias)
    - [Instalar pip](#instalar-pip)
      - [1 - Instalar pip en ubuntu](#1---instalar-pip-en-ubuntu)
      - [2 - Verificar la versión de pip](#2---verificar-la-versión-de-pip)
      - [3 - Actualizar pip](#3---actualizar-pip)
      - [4 - Instalar el virtualenv](#4---instalar-el-virtualenv)
      - [5 - Crear un entorno virtual con virtualenv](#5---crear-un-entorno-virtual-con-virtualenv)
      - [6 - Activar el entorno virtual](#6---activar-el-entorno-virtual)
      - [7 - Instalar dependencias con pip](#7---instalar-dependencias-con-pip)
      - [8 - Instalar dependencias desde el archivo requirements.txt](#8---instalar-dependencias-desde-el-archivo-requirementstxt)
      - [9 - Saliendo del entorno virtual](#9---saliendo-del-entorno-virtual)
    - [Instalar pipenv](#instalar-pipenv)
      - [1 - Instalar pipenv en ubuntu](#1---instalar-pipenv-en-ubuntu)
      - [2 - Verificar la versión de pipenv](#2---verificar-la-versión-de-pipenv)
      - [3 - Crear un entorno virtual con pipenv](#3---crear-un-entorno-virtual-con-pipenv)
      - [4 - Instalar dependencias con pipenv](#4---instalar-dependencias-con-pipenv)
      - [5 - Instalar dependencias desde el archivo requirements.txt](#5---instalar-dependencias-desde-el-archivo-requirementstxt)
      - [6 - Saliendo del entorno virtual de pipenv](#6---saliendo-del-entorno-virtual-de-pipenv)
  - [Configuración](#configuración)
    - [Archivos necesarios para trabajar con la aplicación](#archivos-necesarios-para-trabajar-con-la-aplicación)
    - [Como usar la aplicación](#como-usar-la-aplicación)
      - [Comandos de ayuda](#comandos-de-ayuda)
      - [Comando para buscar datos en archivo XML](#comando-para-buscar-datos-en-archivo-xml)
      - [Comando para formatear archivos XML](#comando-para-formatear-archivos-xml)
      - [Comando para exportar los números de estados de cuenta a un archivo CSV](#comando-para-exportar-los-números-de-estados-de-cuenta-a-un-archivo-csv)
      - [Comando para eliminar datos del archivo XML](#comando-para-eliminar-datos-del-archivo-xml)
      - [Comando para elegir días de mora alzar](#comando-para-elegir-días-de-mora-alzar)
    - [Correr aplicación con el archivo de bash](#correr-aplicación-con-el-archivo-de-bash)
      - [Configurar las variables de entorno](#configurar-las-variables-de-entorno)
      - [Configurar .bashrc_aliases o .zshrc_aliases](#configurar-bashrc_aliases-o-zshrc_aliases)
      - [Ejemplos de como utilizar la aplicación con bash](#ejemplos-de-como-utilizar-la-aplicación-con-bash)
  - [Licencia](#licencia)

## Instalar python 3

Para poder ejecutar el proyecto se necesita instalar **python 3** y es recomendable correr la aplicación en el sistema operativo linux.

### Procedemos a instalar python3 en la distribución de linux Ubuntu

#### 1 - Actualizamos las dependencias y paquetes del sistema

- **Ejecutamos en la terminal el siguiente comando para actualizar el sistema linux**

```shell
sudo apt-get update
```

- **Instalamos las dependencias y paquetes descargados**

```shell
sudo apt-get upgrade
```

- **Confirme la instalación si se le solicita.**

#### 2 - Comprobamos la versión del Python 3

- **Compruebe qué versión de python3 tiene instalada el sistema escribiendo:**

```shell
python3 -V
```

**Otra forma de saber la versión de python.**

```shell
python3 --version
```

> **En caso de que el sistema no imprima la versión del python procedemos instalarlo**

#### 2 - Instalamos Python 3 en el sistema

- Ya con el sistema operativo actualizado procedemos instalar en la terminal el python 3 y ejecutamos el siguiente comando:

```shell
sudo apt install python3
```

> **Confirme la instalación del python3 y al terminar ya podremos saber la versión instalada**

| Nota: para correr la aplicación la versión del Python debe ser igual o superior a python v3.6.9|
| --- |

## Dependencias

Está aplicación utiliza librerías que vienen instaladas por defecto con python3 y serian:

```python
import os
import xml.etree.ElementTree
import xml.dom.minidom
import csv
import random
from sys import argv
from copy import deepcopy
```

- En este caso no se necesita instalar dependencias, pero dejo la guía de como instalar dependencias con el gestor de paquetes pip **(package installer for Python)** y Pipenv **(Python Development Workflow for Humans)**.

### Instalar pip

#### 1 - Instalar pip en ubuntu

- Ejecutamos el siguiente comando en la terminal para instalar pip:

```shell
sudo apt-get install python3-pip
```

> **Confirme la instalación del pip y al terminar ya podremos saber la versión instalada**

#### 2 - Verificar la versión de pip

- Ejecutamos los siguientes comandos para saber la versión de pip instalada:

```shell
python3 -m pip --version
```

**Otra forma de saber la versión de pip.**

```shell
pip --version
```

#### 3 - Actualizar pip

En el caso que pip te sugiera actualizar pip lo puede hacer con el siguiente comando:

```shell
python3 -m pip install --user --upgrade pip
```

#### 4 - Instalar el virtualenv

Para instalar dependencias es necesario crear un entorno virtual para instalar las dependencias, procedemos a instalar el virtualenv:

```shell
python3 -m pip install --user virtualenv
```

#### 5 - Crear un entorno virtual con virtualenv

Para crear un entorno virtual ejecutamos el siguiente comando:

```shell
python3 -m venv env
```

#### 6 - Activar el entorno virtual

Antes de instalar dependencias debemos activar el entorno virtual, para activarlo ejecutamos el siguiente comando:

```shell
source env/bin/activate
```

#### 7 - Instalar dependencias con pip

Con el entorno virtual activado podremos instalar los paquetes que deseamos y lo hacemos de la siguiente manera ejecutando el siguiente comando:

```shell
pip install requests
```

**Otra forma de instalar paquetes con pip.**

```shell
python3 -m pip install requests
```

> **requests** es un ejemplo de una librería para hacer peticiones HTTP

#### 8 - Instalar dependencias desde el archivo requirements.txt

Teniendo activado el entorno virtual, también podemos instalar dependencias que estén en el archivo **requirements.txt** que esté en directorio del proyecto y lo podremos instalar con el siguiente comando:

```shell
pip install -r requirements.txt
```

#### 9 - Saliendo del entorno virtual

Si desea cambiar de proyecto o abandonar su entorno virtual, simplemente ejecute el siguiente comando:

```shell
deactivate
```

> Para más información de como instalar pip puede ir a la documentación de pip : [Documentación de pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

### Instalar pipenv

> Para instalar pipenv debemos tener instalado pip.

Ya teniendo instalado pip procedemos a instalar pipenv

#### 1 - Instalar pipenv en ubuntu

- Ejecutamos el siguiente comando en la terminal para instalar pipenv:

```shell
pip install pipenv
```

Otra forma de instalar pipenv

```shell
python3 -m pip install --user pipenv
```

#### 2 - Verificar la versión de pipenv

- Ejecutamos los siguientes comandos para saber la versión de pipenv instalada:

```shell
pipenv --version
```

#### 3 - Crear un entorno virtual con pipenv

Para crear un entorno virtual debemos estar adentro de la carpeta del proyecto que estemos trabajando y ejecutamos el siguiente comando:

```shell
pipenv shell
```

Esto creará un entorno virtual si aún no existe uno.

#### 4 - Instalar dependencias con pipenv

Con el entorno virtual activado podremos instalar los paquetes que deseamos y lo hacemos de la siguiente manera ejecutando el siguiente comando:

```shell
pipenv install requests
```

> **requests** es un ejemplo de una librería para hacer peticiones HTTP

#### 5 - Instalar dependencias desde el archivo requirements.txt

Teniendo activado el entorno virtual, también podemos instalar dependencias que estén en el archivo **requirements.txt** que esté en directorio del proyecto y lo podremos instalar con el siguiente comando:

```shell
pipenv install -r requirements.txt
```

#### 6 - Saliendo del entorno virtual de pipenv

Si desea cambiar de proyecto o abandonar su entorno virtual, simplemente ejecute el siguiente comando:

```shell
exit
```

> Para más información de como instalar pipenv consultar estos blogs : [Documentación de pipenv](https://docs.pipenv.org/) o [Guía de como instalar pipenv](https://realpython.com/pipenv-guide/)

**En caso de que tenga problemas en instalar pipenv en ubuntu 18.04 pude consultar esta solución:** [install pipenv ubuntu 18.04](https://gist.github.com/planetceres/8adb62494717c71e93c96d8adad26f5c)

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
<ESTADODECUENTA>
 <OBLIGACION>
  <ENCABEZADO>
   <ESTADOCUENTA>12345</ESTADOCUENTA>
  </ENCABEZADO>
 </OBLIGACION>
</ESTADODECUENTA>
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

 **NOTA:**`En la raíz del proyecto, en la carpeta doc/, habrá archivos CSV, XML y días de mora de ejemplo para testear la aplicación.`

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

### Correr aplicación con el archivo de bash

En la raíz del proyecto hay un archivo llamado `script.sh`, con este archivo podremos ejecutar la aplicación sin la necesidad de poner el comando `python3` antes de ejecutar la aplicación, además otras ventajas que tiene de ejecutar la aplicación es que se puede configurar para poder ejecutar la aplicación en cualquier parte del sistema linux, y seguirá recibiendo los mismos parámetros que recibe si lo estuviera tirando desde el directorio raíz, para configurar esté archivo debemos seguir las siguientes instrucciones:

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

> Al final de la ruta debemos poner nombre del archivo `main.py` para que el `script.sh` pueda saber como ejecutar la aplicación

Ya con la variable de entorno definida procedemos configurar el `script.sh` para que el sistema lo pueda leer en cualquier parte del sistema.

#### Configurar .bashrc_aliases o .zshrc_aliases

No dirigimos al `$HOME` de linux `~$:` donde están los archivos `.bashrc` o `.zshrc` y con un editor de texto como `vim` o `nano`, nos dirigimos casi al final del archivo, y el archivo debe tener las siguientes líneas de código:

`.bashrc`

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

**En `.zshrc` debes crear esta líneas de código:**

```zsh
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi
```

Ya verificando que están estas línea de código podremos agregar la aplicación en el archivo `.bashrc_aliases` o `.zshrc_aliases`, y lo hacemos de la siguiente manera, agregando estas líneas de código:

```zsh
# Ejecutar la aplicación xml_data_search
alias script-search-xml=". /home/USER-linux/ruta-donde-clonó-el-repositorio/xml_data_search/script.sh"
```

> Al final de la ruta debemos poner el nombre del archivo `script.sh` para poder ejecutar la aplicación por medio de `BASH`, y también recuerda poner un `.` antes de la ruta para que se pueda ejecutar, y si no te gusta el punto también puede poner el comando `bash`.

Cuando hayas agregado el alias, debes guardar el archivo y luego ejecutar el siguiente comando para que linux pueda reconocer la aplicación en el sistema y el comando sería:

```zsh
# Ejecutar aplicación xml_data_search
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

#### Ejemplos de como utilizar la aplicación con bash

Ya con haber configurado seguido los pasos anteriores, te muestro algunos ejemplos de como utilizar la aplicación por medio del `script.sh` con `bash` y esto son algunos ejemplos:

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
