from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
import os

flag = True
name_file = ""
data_array_csv = []
data_array_xml = []
data_index_xml = []
files = []
csv = Csv()
xml = Xml()


# class Menu(Csv, Xml):
#     def __init__(self):
#         self.flag = True
#         self.name_file = ""
#         Csv.__init__(self)
#         Xml.__init__(self)
#         # super().__init__()

# Método para cargar los datos csv y xml
def get_data_csv_and_xml():
    global name_file
    global data_array_csv
    global data_array_xml
    global data_index_xml
    files_name = get_the_current_working_directory()
    print_files = [print(f"{[files_name.index(item)]}-{item}") for item in files_name]
    try:
        file_csv = int(input("Selecciona el archivo csv: "))
        file_xml = int(input("Selecciona el archivo xml: "))
        if ".csv" in files_name[file_csv] and ".xml" in files_name[file_xml]:
            xml.check_and_format_xml(files_name[file_xml])
            data_array_csv = csv.get_csv_data_list(files_name[file_csv])
            data_array_xml = xml.xml_data_list(files_name[file_xml])
            name_file = files_name[file_xml]
        else:
            print("seleccionaste mal los archivos, debe ser 1 el csv y 2 el xml\n")
    except IndexError as error_index:
        print(f"Error: {error_index} \n")


# Método que imprime el menu que tiene el sistema
def menu():
    global flag
    global name_file
    global data_array_csv
    global data_array_xml
    global data_index_xml
    while flag:
        print('[1]Cargar datos csv y xml')
        print('[2]Buscar datos en estados de cuenta')
        print('[3]Escribir archivo final')
        print('[0]Salir')
        command = str(input('Que deseas hacer \n$:'))
        if command == '1':
            get_data_csv_and_xml()
        elif command == '2':
            data_index_xml = xml.search_the_index_in_the_list(data_array_csv, data_array_xml)
        elif command == '3':
            name_file_xml = xml.write_file_xml()
            xml.build_xml(name_file, name_file_xml, data_index_xml)
        elif command == '0':
            identify_system()
            flag = False
        else:
            identify_system()
            flag = False


# Método para construir el archivo por medio de argumentos por linea de comando
def build_xml_with_arguments(argv):
    print(f"Archivos agregados CSV: {argv[1]} XML: {argv[2]} Name-file: {argv[3]}")
    data_array_csv = csv.get_csv_data_list(argv[1])
    xml.check_and_format_xml(argv[2])
    data_array_xml = xml.xml_data_list(argv[2])
    data_index_xml = xml.search_the_index_in_the_list(data_array_csv, data_array_xml)
    xml.build_xml(argv[2], argv[3], data_index_xml)


# Método para formatear archivos xml por medio de argumentos por linea de comando
def format_xml_with_arguments(argv):
    xml.check_and_format_xml(argv[2])


# Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
def export_data_csv_arguments(argv):
    xml.check_and_format_xml(argv[2])
    data_xml = xml.xml_data_list(argv[2])
    csv.export_data_csv(data_xml, argv[3])


# Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
def remove_xml_values_with_arguments(argv):
    print(f"Archivos agregados CSV: {argv[2]} XML: {argv[3]}")
    data_array_csv = csv.get_csv_data_list(argv[2])
    xml.check_and_format_xml(argv[3])
    data_array_xml = xml.xml_data_list(argv[3])
    data_index_xml = xml.search_the_index_in_the_list(data_array_csv, data_array_xml)
    xml.remove_xml_values(argv[3], data_index_xml)


# Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
def get_the_current_working_directory():
    global files
    cwd = os.getcwd()
    list_files = os.listdir(cwd)
    files = [item for item in list_files if '.csv' in item or '.xml' in item]
    return files


# Método para identificar el sistema operativo para poder limpiar la consola
def identify_system():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')


# Método que imprime el mensaje de inicio del script
def print_message():
    print('B I E N V E N I D O\n')
    print('Nota: verifica que en directorio del proyecto estén los archivos:')
    print('[*.csv y *.xml]')
    print('[Los datos del csv deben estar en una sola columna y solo números]')
    print('[Cargar un archivo csv y xml a la ves]\n')
    print('[El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]\n')


# Método que imprime el mensaje de ayuda para el usuario
def print_message_help():
    print("Descripción: Buscador de datos xml, formateado de xml, exportador a csv, eliminador de datos en el xml\n")
    print("Search data in xml")
    print("position arguments:")
    print(" main.py file-CSV.csv file-XML.xml Name-file-XML.xml\n")
    print("Format xml")
    print("position arguments:")
    print(" main.py -f file-XML.xml\n")
    print("Export data xml to csv")
    print("position arguments:")
    print(" main.py -e file-XML.xml file-CSV.csv\n")
    print("Remove values in xml")
    print("position arguments:")
    print(" main.py -r file-CSV.csv file-XML.xml\n")
    print("opcional arguments:")
    print(" -h, --help  show this help message and exit")
    print(" -f, format xml files")
    print(" -e, export account statement numbers to csv")
    print(" -r, remove account statement")
