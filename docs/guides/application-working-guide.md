# Como funcionan los comandos

Para poder correr la aplicación, se necesitan los archivos XML y CSV, con sus respectivas estructura.

> **NOTA:** En la raíz del proyecto, en la carpeta `docs/`, abran archivos de ejemplo para testear la aplicación.

## Tabla de contenido

- [Como funcionan los comandos](#como-funcionan-los-comandos)
  - [Tabla de contenido](#tabla-de-contenido)
    - [Comandos de ayuda](#comandos-de-ayuda)
    - [Comando para clonar datos en archivo XML](#comando-para-clonar-datos-en-archivo-xml)
    - [Comando para formatear archivos XML](#comando-para-formatear-archivos-xml)
    - [Comando para exportar los id a un archivo CSV](#comando-para-exportar-los-id-a-un-archivo-csv)
    - [Comando para eliminar datos del archivo XML](#comando-para-eliminar-datos-del-archivo-xml)
    - [Comando para elegir las llaves y valores al azar](#comando-para-elegir-las-llaves-y-valores-al-azar)
    - [Comando para exportar múltiples archivos CSV con base en datos en archivos XML](#comando-para-exportar-múltiples-archivos-csv-con-base-en-datos-en-archivos-xml)
    - [Comando para exportar múltiples archivos XML con base en datos del archivo CSV](#comando-para-exportar-múltiples-archivos-xml-con-base-en-datos-del-archivo-csv)
    - [Comando para exportar un solo archivo CSV con base en datos en archivos XML](#comando-para-exportar-un-solo-archivo-csv-con-base-en-datos-en-archivos-xml)
    - [Comando para unir múltiples archivos CSV a un solo archivos CSV](#comando-para-unir-múltiples-archivos-csv-a-un-solo-archivos-csv)
    - [Comando para buscar datos entre multiples archivos XML](#comando-para-buscar-datos-entre-multiples-archivos-xml)
    - [Comando para comparar dos archivos CSV con listas de números iguales y encontrar los duplicados](#comando-para-comparar-dos-archivos-csv-con-listas-de-números-iguales-y-encontrar-los-duplicados)

### Comandos de ayuda

La aplicación tiene un comando de ayuda para poder saber como utilizar la aplicación, para ejecutar el comando de ayuda ejecutamos los siguientes comandos:

```shell
python3 main.py -h
o
python3 main.py --help
o
python3 main.py -man
o
python3 main.py -manual
```

Estos comandos nos mostrar como se puede utilizar la aplicación y que comandos recibe.

### Comando para clonar datos en archivo XML

Con el siguiente comando podremos exportar a un archivo XML, los datos que necesitemos del archivo XML más grande, a un XML más pequeño y con los datos que el usuario le indique.

Ejemplo del directorio con el archivo XML y CSV:

```bash
directorio
├── sample-XML.xml
└── sample-CSV.csv
```

Para exportar los datos ejecutamos el siguiente comando:

```shell
python3 main.py -clone sample-CSV.csv sample-XML.csv name-of-new-XML-file.xml

python3 main.py -c sample-CSV.csv sample-XML.csv name-of-new-XML-file.xml
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-clone) o (-c) ⟵ Bandera que indica a la aplicación que se va a clonar  datos a un nuevo archivo XML.`

`Posición 2 = sample-CSV.csv ⟵ Archivo CSV con los datos a buscar.`

`Posición 3 = sample-XML.csv ⟵ Archivo XML con la información que se va a copiar.`

`Posición 4 = name-of-new-XML-file ⟵ Se ingresa el nombre del nuevo archivo XML.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-XML.xml
├── sample-CSV.csv
└── name-of-new-XML-file.xml
```

### Comando para formatear archivos XML

Con el siguiente comando podremos dar formato a los archivos XML.

Abecés los archivos XML Vienen con la información comprimida, entonces a la aplicación le queda muy difícil leer la información comprimida, entonces con este comando podemos dar formato a los archivos xml que necesite leer la información, para formatear un archivo ejecutamos el siguiente comando:

```shell
python3 main.py -format XML-file-to-format.xml
o
python3 main.py -f XML-file-to-format.xml
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-format) o (-f) ⟵ Bandera que indica a la aplicación que se necesita formatear el archivo xml.`

`Posición 2 = XML-file-to-format.xml ⟵ Archivo XML al que se va a formatear.`

### Comando para exportar los id a un archivo CSV

Con el siguiente comando podremos exportar los id a un archivo CSV.

Ejemplo del directorio con el archivo XML:

```bash
directorio
└── sample-XML.xml
```

Si el usuario los desea puede exportar todos los id que estén en el archivo XML a un archivo CSV, para exportarlos ejecutamos el siguiente comando:

```shell
python3 main.py -export sample-XML.xml name-of-new-CSV-file.csv
o
python3 main.py -e sample-XML.xml name-of-new-CSV-file.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-export) o (-e) ⟵ Bandera que indica a la aplicación que se necesita exportar los datos.`

`Posición 2 = sample-XML.xml ⟵ Archivo XML donde está la información a exportar.`

`Posición 3 = name-of-new-CSV-file.csv ⟵ Se ingresa el nombre que va a tener el archivo CSV donde se va a exportar la información.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-XML.xml
└── name-of-new-CSV-file.csv
```

### Comando para eliminar datos del archivo XML

Con el siguiente comando podremos eliminar datos del archivo XML.

Si el usuario necesitar eliminar una N cantidad de datos del archivo XML, lo puede hacer utilizando [la misma forma de como se buscan los datos](##comando-para-clonar-datos-en-archivo-xml), pero esta vez la aplicación buscar los id y los eliminará, para eliminar los datos debemos ejecutar el siguiente comando:

```shell
python3 main.py -remove sample-CSV.csv sample-XML.csv
o
python3 main.py -r sample-CSV.csv sample-XML.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-remove) o (-r) ⟵ Bandera que indica a la aplicación que se necesita remover datos.`

`Posición 3 = CSV-name.csv ⟵ Archivo CSV con los id que se necesitan eliminar.`

`Posición 2 = sample-XML.csv ⟵ Archivo XML donde está la información que se va a eliminar.`

**Cuando termine la aplicación de eliminar los datos verifica que se hayan eliminado los datos que le indicaste en el archivo CSV.**

### Comando para elegir las llaves y valores al azar

Con el siguiente comando podremos elegir las llaves y valores al azar.

Ejemplo del directorio con el archivo CSV con las llaves y valores:

```bash
directorio
└── sample-key-value.csv
```

Si el usuario desea elegir N llaves y valores al azar, el sistema tomara un número que indique el usuario y el generar esa cantidad de llaves y valores y los imprime en consola, lo pude hacer con el siguiente comando:

```shell
python3 main.py -random-access-value sample-key-value.csv number
o
python3 main.py -rav sample-key-value.csv number
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-random-access-value) (-rav) ⟵ Bandera que indica a la aplicación que se van a seleccionar llaves y valores al azar.`

`Posición 3 = sample-key-value.csv ⟵ Archivo CSV con las llaves y valores que se van a seleccionar al azar.`

`Posición 2 = number ⟵ Se ingresa el número que desear imprimir ejemplo: 5.`

Ejemplo de como mostrara la aplicación en la terminal las llaves y valores al azar:

```bash
KEY | VALUE
43210 | 60
00034 | 20
00056 | 10
98765 | 10
00123 | 20
```

### Comando para exportar múltiples archivos CSV con base en datos en archivos XML

Con el siguiente comando podremos exportar varios archivos CSV con datos de los archivos XML que estén en el directorio que le indiquen.

Si el usuario necesita exportar múltiples archivos CSV con datos que contengan los archivos XML que estén en un directorio, digamos que los archivos XML son diferentes y necesitan exportar esos datos a archivos CSV, la aplicación puede hacerlo, al momento de generar los archivos CSV tomara la etiqueta que le indiquen en el archivo de configuración, con el texto que contenga está etiqueta creara el nombre de los archivos CSV.

Ejemplo del directorio con los archivos XML:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
└── sample-XML-3.xml
```

Ejemplo de como buscaría la aplicación:

La aplicación buscará todas las etiquetas que estén el archivo XML:

```xml
# Ejemplo
<id>12345</id>
```

Luego de recolectar todos los textos que tengan estas etiquetas, buscara la siguiente etiqueta y obtendrá el texto, y con este texto la aplicación crear el nombre del archivo CSV:

```xml
# Ejemplo
<product>product_1</product>
```

El nombre que elegiría la aplicación seria `product_1.csv`, como son varios archivos XML en el directorio que le indiquen, la aplicación para evitar sobrescriba archivos CSV, les agrega números al final del nombre como ejemplo `product_11.csv`.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -export-csv PATH-DIRECTORY
o
python3 main.py -ec PATH-DIRECTORY
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-export-csv) (-ec) ⟵ Bandera que indica a la aplicación que se van a exportar múltiples archivos CSV.`

`Posición 2 = PATH-DIRECTORY ⟵ Se indica el directorio(carpeta) en donde estén los archivos XML, y en ese mismo directorio se crearan los archivos CSV.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
├── sample-XML-3.xml
├── product_1.csv
├── product_2.csv
└── product_3.csv
```

### Comando para exportar múltiples archivos XML con base en datos del archivo CSV

Con el siguiente comando podremos exportar varios archivos XML con datos del archivo CSV que estén en el directorio que le indiquen.

Si el usuario necesita exportar múltiples archivos XML basado en la lista de datos que tenga el archivo CSV, digamos que en el directorio que le indiquen a la aplicación hay varios archivos XML, pero tu tienes una lista de datos en el archivo CSV, pero esto datos están en desorden, la aplicación buscara data por dato y encontrar el archivo que pertenece ese dato y los agrupara si son del mismo producto

Ejemplo del directorio con archivos XML y el archivo CSV:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
├── sample-XML-3.xml
└── sample-csv.csv
```

Ejemplo de como buscaría la aplicación:

La aplicación buscará todas las etiquetas que estén el archivo XML:

```xml
# Ejemplo
<id>12345</id>
```

Luego de recolectar todos los textos que tengan estas etiquetas, buscara la siguiente etiqueta y obtendrá el texto, y con este texto la aplicación crear el nombre del los archivos XML:

```xml
# Ejemplo
<product>product_1</product>
```

El nombre que elegiría la aplicación seria `product_1.xml`, como son varios archivos XML en el directorio que le indiquen, la aplicación para evitar sobrescriba archivos XML, les agrega números al final del nombre como ejemplo `product_11.xml`.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -export-xml PATH-DIRECTORY sample-csv.csv
o
python3 main.py -ex PATH-DIRECTORY sample-csv.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-export-xml) (-ex) ⟵ Bandera que indica a la aplicación que se van a exportar múltiples archivos XML.`

`Posición 2 = PATH-DIRECTORY ⟵ Se indica el directorio(carpeta) en donde estén los archivos XML, y en ese mismo directorio se clonaran los otros archivos XML.`

`Posición 3 = sample-csv.csv ⟵ Archivo CSV con los datos a buscar.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
├── sample-XML-3.xml
├── sample-csv.csv
├── product_11.xml
├── product_22.xml
└── product_33.xml
```

### Comando para exportar un solo archivo CSV con base en datos en archivos XML

Con el siguiente comando podremos exportar múltiples datos que estén en los archivos XML a un solo archivo CSV, que estén en el directorio que le indiquen.

Si el usuario necesita exportar múltiples datos, de varios archivos XML, lo puede hacer con este comando, es similar al [comando de exportar varios archivos CSV](#comando-para-exportar-múltiples-archivos-csv-con-base-en-datos-en-archivos-xml), pero con la excepción que este comando no exporta varios archivos, si no que exporta todos los datos a un solo archivo CSV, el usuario solo le debe indicar el nombre que va a tener el nombre del archivo CSV con todos los datos.

Ejemplo del directorio con los archivos XML:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
└── sample-XML-3.xml
```

Ejemplo de como buscaría la aplicación:

La aplicación buscará todas las etiquetas que estén el archivo XML:

```xml
# Ejemplo
<id>12345</id>
```

Luego de recolectar todos los textos que tengan estas etiquetas, los agrupara y los exportara en un archivo CSV.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -export-all PATH-DIRECTORY name-of-new-CSV-file.csv
o
python3 main.py -ea PATH-DIRECTORY name-of-new-CSV-file.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-export-all) (-ea) ⟵ Bandera que indica a la aplicación que se van a exportar múltiples datos XML al archivo CSV.`

`Posición 2 = PATH-DIRECTORY ⟵ Se indica el directorio(carpeta) en donde estén los archivos XML, y en ese mismo directorio se guardara el archivo CSV.`

`Posición 3 = name-of-new-CSV-file.csv ⟵ Se ingresa el nombre que va a tener el archivo CSV donde se va a exportar la información.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-XML-1.xml
├── sample-XML-2.xml
├── sample-XML-3.xml
└── name-of-new-CSV-file.csv
```

### Comando para unir múltiples archivos CSV a un solo archivos CSV

Con el siguiente comando podremos unir múltiples archivos CSV que estén en el directorio que le indiquen, y luego de leer todos los datos que estén en los archivos, combinara todos estos datos y los guardara en un archivo CSV, que contenga todos los datos.

Ejemplo del directorio con los archivos CSV:

```bash
directorio
├── sample-CSV-1.csv
├── sample-CSV-2.csv
└── sample-CSV-3.csv
```

La aplicación leerá todos los datos que estén en los archivos CSV uno por uno, y recolectará todos los datos que tengas los archivos CSV.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -merge-csv-files PATH-DIRECTORY name-of-new-CSV-file.csv
o
python3 main.py -mcf PATH-DIRECTORY name-of-new-CSV-file.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-merge-csv-files) (-mcf) ⟵ Bandera que indica a la aplicación que se van a unir múltiples datos CSV al un solo archivo CSV.`

`Posición 2 = PATH-DIRECTORY ⟵ Se indica el directorio(carpeta) en donde estén los archivos CSV, y en ese mismo directorio se guardara el archivo CSV.`

`Posición 3 = name-of-new-CSV-file.csv ⟵ Se ingresa el nombre que va a tener el archivo CSV donde se va a exportar la información.`

Ejemplo de como quedaría los archivos en el directorio:

```bash
directorio
├── sample-CSV-1.csv
├── sample-CSV-2.csv
├── sample-CSV-3.csv
└── name-of-new-CSV-file.csv
```

### Comando para buscar datos entre multiples archivos XML

Con el siguiente comando podremos buscar un dato en especifico que necesitemos y no sabemos en que archivo XML está de los multiples archivos XML estén en el directorio que le especifiquen a la aplicación.

Digamos que tienes el número de `<id>12345</id>`, pero no sabes en cual de los multiples archivos XML está este datos, con el siguiente comando podrás saber en cual de los múltiples archivos XML esta este dato.

Ejemplo del directorio con los archivos XML:

```bash
directorio
├──1
|  ├── sample-XML-1.xml
|  └── sample-XML-2.xml
├──2
|  ├── sample-XML-3.xml
|  └── sample-XML-4.xml
├──3
|  ├── sample-XML-5.xml
|  └── sample-XML-6.xml
├── sample-XML-7.xml
└── sample-XML-8.xml
```

La aplicación tiene la capacidad de buscar recursivamente los archivos XML, y buscará uno por uno el dato que necesites encontrar y el archivo que almacena esta información.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -search-data PATH-DIRECTORY DATA-TO_SEARCH
o
python3 main.py -sd PATH-DIRECTORY DATA-TO_SEARCH
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-search-data) (-sd) ⟵ Bandera que indica a la aplicación que se van a buscar entre múltiples archivos XML un dato que el usuario le indique.`

`Posición 2 = PATH-DIRECTORY ⟵ Se indica el directorio(carpeta) en donde estén los archivos XML.`

`Posición 3 = DATA-TO_SEARCH ⟵ Se ingresa el dato que se desea buscar el usuario, ejemplo: 12345.`

Ejemplo de como mostrara la aplicación en la terminal si encuentra el dato que le indico el usuario:

```shell
► id → 556677
► number → 00001
► product → product_1
► name → pedro
► reference → 12345
► XML-PATH → ./2/sample-XML-3.xml
```

### Comando para comparar dos archivos CSV con listas de números iguales y encontrar los duplicados

Con el siguiente comando podremos comparar dos listas de datos CSV y encontrar los datos que se repiten en ambas listas numéricas

Digamos que el archivo CSV `sample-CSV-1.csv` tenemos los siguientes datos:

| |
|-|
|1|
|2|
|3|
|4|
|5|

Y en el archivo CSV `sample-CSV-2.csv` tenemos los siguientes datos:

| |
|-|
|6|
|7|
|8|
|5|
|9|

La aplicación va comparar estas dos listas de datos y como ejemplo encontrara que el número `5` se repite en las dos listas, y este número lo guardara en un nuevo archivo CSV, en caso de haber más números similares, también los guardara en el archivo CSV `exporting-duplicates.csv`.

Para realizar este proceso ejecuta el siguiente comando:

```shell
python3 main.py -compare sample-CSV-1.csv sample-CSV-2.csv
o
python3 main.py -C sample-CSV-1.csv sample-CSV-2.csv
```

`Posición 0 = main.py ⟵ Archivo con el que se inicia la aplicación.`

`Posición 1 = (-compare) (-C) ⟵ Bandera que indica a la aplicación que se van a comparar, dos archivos CSV, para encontrar los datos duplicados.`

`Posición 2 = sample-CSV-1.csv ⟵ Archivo CSV con la lista de datos a comparar.`

`Posición 3 = sample-CSV-2.csv ⟵ Archivo CSV con la lista de datos que estén duplicados.`

Ejemplo de como mostrara la aplicación en la terminal si encuentra los datos duplicados:

```shell
Total datos repetidos: 1
Los datos duplicados se agregaron al archivo: exporting-duplicates.csv
```
