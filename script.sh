# !/bin/bash
# Script para ejecutar el projecto xml_data_search

# Directorio donde esta el script de python
# En esta parte agregas la ruta donde se clona o se pone el proyecto ejemplo:
#PATH_SCRIPT="/ruta/donde/clonas/el/proyecto/main.py"
PATH_SCRIPT=""

# Variables donde capturan los argumentos que resive el script.sh
FLAG=$1
FILE_1=$1
FILE_2=$2
FILE_3=$3

# Banderas que tiene el script
FORMAT=-f
EXPORT=-e
REMOVE=-r
HELP=-h

# Directorio actual
CURRENT_PATH=$(pwd)

# Parametros para buscar con Regex y validar que sean archivos .csv y .xml
CSV='.csv'
XML='.xml'

# Comando para ejecutar los script en python 3
COMMAND_PYTHON=python3

# Validar los parametros que envie el usuario
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

# Evalua que el script se halla ejecutado bien
# Code status 0 = bien
if [ $? -eq 0 ]; then
	echo "OK, Se ejecuto el script con normalidad"
else
	echo "ERROR: no se pudo ejecutar el script de python"
fi
