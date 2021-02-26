#!/bin/bash
# Script para ejecutar el proyecto xml_data_search.

# Con estas dos líneas obtenemos el directorio donde se está ejecutando el proyecto.
SCRIPT=$(readlink -f $0);
dir_base=`dirname $SCRIPT`;

if [ -f $dir_base/.env ]; then
	# Carga las variables de entorno
	export $(grep -v '^#' $dir_base/.env | xargs)
	# export $(cat $dir_base/.env | grep -v '#' | awk '/=/ {print $1}')
	# Se cargan las variables de entorno que esté en el archivo .env:
	#PATH_SCRIPT="/ruta/donde/clonas/el/proyecto/main.py"
fi

# Variables donde capturan los argumentos que recibe el script.sh.
FLAG=$1
FILE_1=$1
FILE_2=$2
FILE_3=$3

# Banderas que tiene la aplicación.
FORMAT=-f
EXPORT=-e
REMOVE=-r
HELP=-h

# Directorio actual.
CURRENT_PATH=$(pwd)

# Parámetros para buscar con Regex y validar que sean archivos .csv y .xml.
CSV='.csv'
XML='.xml'

# Comando para ejecutar los script en python 3.
COMMAND_PYTHON=python3

# Validar los parámetros que envié el usuario.
if [[ $FLAG == $FORMAT ]]; then
	$COMMAND_PYTHON $PATH_SCRIPT $FORMAT "$CURRENT_PATH/$FILE_2"
elif [[ $FLAG == $EXPORT ]]; then
	$COMMAND_PYTHON $PATH_SCRIPT $EXPORT "$CURRENT_PATH/$FILE_2" "$CURRENT_PATH/$FILE_3"
elif [[ $FLAG == $REMOVE ]]; then
	$COMMAND_PYTHON $PATH_SCRIPT $REMOVE "$CURRENT_PATH/$FILE_2" "$CURRENT_PATH/$FILE_3"
elif [[ $FLAG == $HELP ]]; then
	$COMMAND_PYTHON $PATH_SCRIPT $HELP
elif [[ $FILE_1 =~ ($CSV)$ ]] && [[ $FILE_2 =~ ($XML)$ ]] && [[ $FILE_3 =~ ($XML)$ ]]; then
	$COMMAND_PYTHON $PATH_SCRIPT "$CURRENT_PATH/$FILE_1" "$CURRENT_PATH/$FILE_2" "$CURRENT_PATH/$FILE_3"
else
	$COMMAND_PYTHON $PATH_SCRIPT
fi

# Evalúa que el script se halla ejecutado bien.
# Code status 0 = bien
if [ $? -eq 0 ]; then
	echo "OK, Se ejecuto el script con normalidad"
else
	echo "ERROR: no se pudo ejecutar el script de python"
fi
