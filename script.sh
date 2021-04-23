#!/bin/bash
# Script para ejecutar el proyecto xml_data_search.

# Con estas dos líneas obtenemos el directorio donde se está ejecutando el proyecto.
SCRIPT=$(readlink -f "$0");
dir_base=$(dirname "$SCRIPT");

if [ -f "$dir_base"/.env ]; then
	# Carga las variables de entorno
	export $(grep -v '^#' $dir_base/.env | xargs)
	# export $(cat $dir_base/.env | grep -v '#' | awk '/=/ {print $1}')
	# Se cargan las variables de entorno que esté en el archivo .env:
	#PATH_SCRIPT="/ruta/donde/clonas/el/proyecto/main.py"
fi

# Comando para ejecutar los script en python 3.
COMMAND_PYTHON=python3

# Ejecutar aplicación
$COMMAND_PYTHON "$PATH_SCRIPT" "$@"

# Evalúa que el script se halla ejecutado bien.
# Code status 0 = bien
if [ $? -eq 0 ]; then
	echo "OK, Se ejecutó el script.sh con normalidad"
else
	echo "ERROR: no se pudo ejecutar la aplicación de python o el script.sh"
fi
