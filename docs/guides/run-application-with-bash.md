# Correr aplicación con el archivo de Bash

En la raíz del proyecto hay un archivo llamado `script.sh`, con este archivo podremos ejecutar la aplicación sin la necesidad de poner el comando `python3` antes de ejecutar la aplicación, además otras ventajas que tiene de ejecutar la aplicación es que se puede configurar para poder ejecutar la aplicación en cualquier parte del sistema Linux, y seguirá recibiendo los mismos parámetros que recibe si lo estuviera tirando desde el directorio raíz, para configurar esté archivo debemos seguir las siguientes instrucciones:

## Tabla de contenido

- [Correr aplicación con el archivo de Bash](#correr-aplicación-con-el-archivo-de-bash)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Configurar las variables de entorno](#configurar-las-variables-de-entorno)
    - [Agregar permiso de ejecución](#agregar-permiso-de-ejecución)
    - [Configurar .bashrc_aliases o .zshrc_aliases](#configurar-bashrc_aliases-o-zshrc_aliases)
    - [Ejemplos de como utilizar la aplicación con Bash](#ejemplos-de-como-utilizar-la-aplicación-con-bash)

## Configurar las variables de entorno

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

### Agregar permiso de ejecución

Al archivo `script.sh` se le debe agregar el permiso de ejecución, para que se pueda ejecutar, para agregar el permiso ejecutamos el siguiente comando:

```sh
chmod +x script.sh
```

### Configurar .bashrc_aliases o .zshrc_aliases

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

### Ejemplos de como utilizar la aplicación con Bash

Ya con haber configurado y seguido los pasos anteriores, te muestro algunos ejemplos de como utilizar la aplicación por medio del `script.sh` con `Bash` y esto son algunos ejemplos:

```zsh
# Con estos comandos imprimes en la terminal las ayudas de la aplicación:
script-search-xml -h
script-search-xml --help
script-search-xml --man
script-search-xml --manual

# Con este comando podrás clonar los datos XML a uno nuevo:
script-search-xml -clone sample-CSV.csv sample-XML.xml name-of-new-XML-file.xml
o
script-search-xml -c sample-CSV.csv sample-XML.xml name-of-new-XML-file.xml

# Con este comando podrás formatear los archivos XML:
script-search-xml -format XML-file-to-format.xml
o
script-search-xml -f XML-file-to-format.xml

# Con este comando podrás exportar múltiples ID a un archivo CSV:
script-search-xml -export sample-XML.xml name-of-new-CSV-file.csv
o
script-search-xml -e sample-XML.xml name-of-new-CSV-file.csv

# Con este comando podrás borrar datos del archivo XML:
script-search-xml -remove sample-CSV.csv sample-XML.xml
o
script-search-xml -r sample-CSV.csv sample-XML.xml

# Con este comando podrás elegir llaves y valores al azar:
script-search-xml -random-access-value sample-key-value.csv (number) <- int
o
script-search-xml -rav sample-key-value.csv (number) <- int

# Con este comando podrás exportar múltiples archivos CSV basado,
# en múltiples archivos XML:
script-search-xml -export-csv PATH-DIRECTORY
o
script-search-xml -ec PATH-DIRECTORY

# Con este comando podrás exportar múltiples archivos XML basado,
# en múltiples datos del archivo CSV, en el directorio,
# que le especifiquen:
script-search-xml -export-xml PATH-DIRECTORY sample-csv.csv
o
script-search-xml -ex PATH-DIRECTORY sample-csv.csv

# Con este comando podrás exportar un solo archivo CSV con múltiples,
# datos de los múltiples datos de los archivos XML en el directorio,
# que le especifiquen:
script-search-xml -export-all PATH-DIRECTORY name-of-new-CSV-file.csv
o
script-search-xml -ea PATH-DIRECTORY name-of-new-CSV-file.csv

# Con este comando podrás unir múltiples archivos CSV en el directorio,
# que le especifiquen y guardara todos los datos que recolecte en un solo,
# archivo CSV:
script-search-xml -merge-csv-files PATH-DIRECTORY name-of-new-CSV-file.csv
o
script-search-xml -mcf PATH-DIRECTORY name-of-new-CSV-file.csv

# Con este comando podrás buscar el ID entre múltiples archivos XML,
# que estén en el directorio que le indiquen y si encuentra el dato,
# mostrar en la terminal la información que encuentre:
script-search-xml -search-data PATH-DIRECTORY DATA-TO_SEARCH
o
script-search-xml -sd PATH-DIRECTORY DATA-TO_SEARCH

# Con este comando podrás comparar dos lista de datos CSV,
# y exportará los datos duplicados a un archivo CSV:
script-search-xml -compare sample-CSV-1.csv sample-CSV-2.csv
o
script-search-xml -C sample-CSV-1.csv sample-CSV-2.csv

# Con este comando podrás comparar dos lista de datos CSV,
# y imprimir en pantalla los polizones:
script-search-xml -stowaway sample-CSV-1.csv sample-CSV-2.csv
o
script-search-xml -S sample-CSV-1.csv sample-CSV-2.csv
```
