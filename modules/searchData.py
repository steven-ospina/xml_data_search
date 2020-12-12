import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
import csv
import os
from copy import deepcopy


class Data:

    def __init__(self):
        self.data_array_xml = []
        self.data_array_csv = []
        self.data_index_xml = []
        self.files = []
        self.flag = True
        self.read_method = 'r'
        self.write_method = 'w'
        self.name_file = ""
        self.name_file_xml = ""

    # Método encargado de escribir los archivos en el sistema
    def write_file_xml(self):
        print("Recuerda poner al final del nombre la extensión *.xml")
        self.name_file_xml = str(input(f"Nombre del archivo\n:"))
        try:
            answer = str(input(f"El nombre del archivo es: {self.name_file_xml} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                self.name_file_xml = self.name_file_xml
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error:
            print('Error: ', error)

        return self.name_file_xml

    # Método encargado de leer los datos que están en el archivo csv
    def get_csv_data_list(self, name_file):
        try:
            with open(name_file, self.read_method) as (File):
                reader = csv.reader(File)
                self.data_array_csv = [''.join(item) for item in reader if item]
                print(f"\nTotal datos csv: {len(self.data_array_csv)}\n")
        except Exception as error:
            print('No se pudo cargar los datos del csv', error)

        return self.data_array_csv

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def xml_data_list(self, name_file):
        root = ET.parse(name_file).getroot()
        self.data_array_xml = [item.find('ESTADOCUENTA').text for item in root.findall(f"./OBLIGACION/ENCABEZADO")]
        print(f"\nTotal estados de cuenta xml: {len(self.data_array_xml)}")

        return self.data_array_xml

    # Método encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self, data_array_csv, data_array_xml):
        try:
            self.data_index_xml = [data_array_xml.index(item) for item in data_array_csv]
            print(f"\nTotal indexes encontrados: {len(self.data_index_xml)}\n")
        except Exception as error:
            print("Error, al buscar el index en el xml, puede ser que los datos en el CSV tengan un espacio: ", error)

        return self.data_index_xml

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, name_file, name_file_xml, data_index_xml):
        try:
            tree = self.build_root_xml(name_file_xml)
            root_source_file = ET.parse(name_file).getroot()
            counter = 0
            obligacion_source_file = [root_source_file[value] for value in data_index_xml]
            obligacion_copy = [deepcopy(value) for value in obligacion_source_file]
            for value in obligacion_copy:
                tree.append(value)
                counter = counter + 1
                print(f"Datos cargando: {counter}", end="\r")

            root_fie_new = ET.ElementTree(tree).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
        except Exception as error:
            print("Error, al escribir el archivo final xml", error)

        print(f"\nTotal datos: [{len(self.data_index_xml)}] escritos en el archivo: {name_file_xml}\n")
        self.name_file = ""

    # Método para crear la root de archivo xml
    def build_root_xml(self, name_file_xml):
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.ElementTree(ESTADODECUENTA).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
            return ET.parse(name_file_xml).getroot()
        except Exception as error:
            print(f"ERROR, no se pudo crear el archivo copia {error}")
            exit(f"ERROR {error}")

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self):
        cwd = os.getcwd()
        list_files = os.listdir(cwd)
        self.files = [item for item in list_files if '.csv' in item or '.xml' in item]

        return self.files

    # Método para cargar los datos csv y xml
    def get_data_csv_and_xml(self):
        files_name = self.get_the_current_working_directory()
        print_files = [print(f"{[files_name.index(item)]}-{item}") for item in files_name]
        try:
            file_csv = int(input("Selecciona el archivo csv: "))
            file_xml = int(input("Selecciona el archivo xml: "))
            if ".csv" in files_name[file_csv] and ".xml" in files_name[file_xml]:
                self.check_and_format_xml(files_name[file_xml])
                self.get_csv_data_list(files_name[file_csv])
                self.xml_data_list(files_name[file_xml])
                self.name_file = files_name[file_xml]
            else:
                print("seleccionaste mal los archivos, debe ser 1 el csv y 2 el xml\n")
        except IndexError as error_index:
            print(f"Error: {error_index} \n")

    # Método para chequear y dar formato al archivo xml
    def check_and_format_xml(self, name_file_xml):
        try:
            with open(name_file_xml) as check_xml:
                reader = check_xml.readline()
                check_format = "\n" in reader
                if(check_format is not True):
                    with open(name_file_xml) as xmldata:
                        print(f"Formateando el archivo {name_file_xml}")
                        xml = DOM.parseString(xmldata.read())
                        xml_pretty_byte = xml.toprettyxml(encoding="utf-8")
                        # Convertir bytes en una cadena y eliminar el extraño problema de la nueva línea
                        xml_pretty_str = os.linesep.join([item for item in xml_pretty_byte.decode("utf-8").splitlines() if item.strip()])
                        # Formatear el archivo xml
                        with open(name_file_xml, self.write_method) as file_out:
                            file_out.write(xml_pretty_str)
                else:
                    return print("El archivo ya esta formateado")
        except Exception as error:
            print(f"Error: {error}, no se pudo formatear el archivo xml \n")

    # Método para exportar los estados de cuenta a un archivo csv
    def export_data_csv(self, data_array_xml, name_file_csv):
        try:
            with open(name_file_csv, self.write_method, newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for data in data_array_xml:
                    csvwriter.writerow([data])
        except Exception as error:
            print(f"Error al exportar los datos xml a csv: {error}")

    # Método para borra datos del archivo xml
    def remove_xml_values(self, name_file, data_index_xml):
        try:
            root_file_xml = ET.parse(name_file).getroot()
            value_to_remove = [root_file_xml[value] for value in data_index_xml]
            print(len(value_to_remove))
            counter = 0
            for value in value_to_remove:
                root_file_xml.remove(value)
                counter = counter + 1
                print(f"Datos eliminados: {counter}", end="\r")

            update_file_xml = ET.ElementTree(root_file_xml).write(name_file, encoding="UTF-8", xml_declaration=True)
            print(f"\nTotal datos eliminados: [{len(self.data_index_xml)}] del archivo: {name_file}\n")

        except Exception as error:
            print(f"Error: al intentar eliminar los elementos del xml, descripción: {error}")

    # Método que imprime el menu que tiene el sistema
    def menu(self):
        while self.flag:
            print('[1]Cargar datos csv y xml')
            print('[2]Buscar datos en estados de cuenta')
            print('[3]Escribir archivo final')
            print('[0]Salir')
            command = str(input('Que deseas hacer \n$:'))
            if command == '1':
                self.get_data_csv_and_xml()
            elif command == '2':
                self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
            elif command == '3':
                self.write_file_xml()
                self.build_xml(self.name_file, self.name_file_xml, self.data_index_xml)
            elif command == '0':
                self.identify_system()
                self.flag = False
            else:
                self.identify_system()
                self.flag = False

    # Método para identificar el sistema operativo para poder limpiar la consola
    def identify_system(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')

    # Método que imprime el mensaje de inicio del script
    def print_message(self):
        print('B I E N V E N I D O\n')
        print('Nota: verifica que en directorio del proyecto estén los archivos:')
        print('[*.csv y *.xml]')
        print('[Los datos del csv deben estar en una sola columna y solo números]')
        print('[Cargar un archivo csv y xml a la ves]\n')
        print('[El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]\n')

    # Método que imprime el mensaje de ayuda para el usuario
    def print_message_help(self):
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

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, argv):
        print(f"Archivos agregados CSV: {argv[1]} XML: {argv[2]} Name-file: {argv[3]}")
        self.get_csv_data_list(argv[1])
        self.check_and_format_xml(argv[2])
        self.xml_data_list(argv[2])
        self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
        self.build_xml(argv[2], argv[3], self.data_index_xml)

    # Método para formatear archivos xml por medio de argumentos por linea de comando
    def format_xml_with_arguments(self, argv):
        self.check_and_format_xml(argv[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, argv):
        self.check_and_format_xml(argv[2])
        data_xml = self.xml_data_list(argv[2])
        self.export_data_csv(data_xml, argv[3])

    # Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
    def remove_xml_values_with_arguments(self, argv):
        print(f"Archivos agregados CSV: {argv[2]} XML: {argv[3]}")
        self.get_csv_data_list(argv[2])
        self.check_and_format_xml(argv[3])
        self.xml_data_list(argv[3])
        self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
        self.remove_xml_values(argv[3], self.data_index_xml)
