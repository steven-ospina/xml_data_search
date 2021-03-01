# Búsqueda de datos xml

![dependencies](https://img.shields.io/badge/python-v3.6.9-blue.svg)
![Current Version](https://img.shields.io/badge/version-0.8.4-green.svg)

Este aplicación se diseño para leer archivos XML y CSV, abecés el archivo XML es muy grande y se necesita buscar N cantidad de datos que manual mente como humanos nos podemos demora mucho, con esta aplicación nos ahorramos el tiempo de formatear el archivo y buscar esos datos, ademas también podemos exportar un dato importante a un archivo csv, para usarlo a la necesidad del usuario.

## Tabla de contenido

- [Instalar python 3](#Instalar-Python3)
- [Dependencias](#dependencias)
  - [instalar pip](#instalar-pip)
  - [instalar pipenv](#instalar-pipenv)
<!-- - [Ejecutar la aplicación](#a) -->

### Instalar python 3

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

**Otra forma de saver la versión de python.**

```shell
python3 --version
```

> **En caso que el sistema no imprima la versión del python procedemos instalarlo**

#### 2 - Instalamos Python 3 en el sistema

- Ya con el sistema operativo actualizado procedemos instalar el la terminal el python 3 y ejecutamos el siguiente comando:

```shell
sudo apt install python3
```

> **Confirme la instalación del python3 y al terminar ya podremos saber la versión instalada**

| Nota: para correr la aplicación la versión del Python debe ser igual o superior a python v3.6.9|
| --- |

### Dependencias

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
sudo apt-get install python3-píp
```

> **Confirme la instalación del pip y al terminar ya podremos saber la versión instalada**

#### 2 - Verificar la versión de pip

- Ejecutamos los siguientes comandos para saber la versión de pip instalada:

```shell
python3 -m pip --version
```

**Otra forma de saver la versión de pip.**

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

#### 5 - crear un entorno virtual con virtualenv

Para crear un entorno virtual ejecutamos el siguiente comando:

```shell
python3 -m venv env
```

#### 6 - activar el entorno virtual

Antes de instalar dependencias debemos activar el entorno virtual, para activarlo ejecutamos el siguiente comando:

```shell
source env/bin/activate
```

#### 7 - Instalar dependencias con pip

Con el entorno virtual activado podremos instalar los paquetes que deseamos y lo hacemos de la siguiente manera ejecutando el siguiente comando:

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

> Para mas información de como instalar pip puede ir a la documentación de pip : [Documentación de pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

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

#### 3 - crear un entorno virtual con pipenv

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

> Para mas información de como instalar pipenv consultar estos blogs : [Documentación de pipenv](https://docs.pipenv.org/) o [Guía de como instalar pipenv](https://realpython.com/pipenv-guide/)

**En caso de que tenga problemas en instalar pipenv en ubuntu 18.04 pude consultar esta solución:** [install pipenv ubuntu 18.04](https://gist.github.com/planetceres/8adb62494717c71e93c96d8adad26f5c)
