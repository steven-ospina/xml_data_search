import xml.etree.ElementTree as ET
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
        self.reading_method = 'r'
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
            with open(name_file, self.reading_method) as (File):
                reader = csv.reader(File)
                self.data_array_csv = [''.join(x) for x in reader]
                print(f"\nTotal datos csv: {len(self.data_array_csv)}\n")
        except Exception as error:
            print('No se pudo cargar los datos del csv', error)

        return self.data_array_csv.sort()

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def xml_data_list(self, name_file):
        root = ET.parse(name_file).getroot()
        self.data_array_xml = [x.find('ESTADOCUENTA').text for x in root.findall(f"./OBLIGACION/ENCABEZADO")]
        print(f"\nTotal estados de cuenta xml: {len(self.data_array_xml)}\n")

        return self.data_array_xml

    # Método encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self, data_array_csv, data_array_xml):
        try:
            self.data_index_xml = [data_array_xml.index(x) for x in data_array_csv]
            print(f"\nTotal datos encontrados: {len(self.data_index_xml)}\n")
        except Exception as error:
            print("Error, al buscar el index en el xml: ", error)

        return self.data_index_xml

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, name_file, name_file_xml, data_index_xml):
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            root_fie_new = ET.ElementTree(ESTADODECUENTA).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
            root_source_file = ET.parse(name_file).getroot()
            tree = ET.parse(name_file_xml).getroot()
            counter = 0
            for i in self.data_index_xml:
                obligacion_source_file = root_source_file[i]
                obligacion_copy = deepcopy(obligacion_source_file)
                tree.append(obligacion_copy)
                root_fie_new = ET.ElementTree(tree).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
                counter = counter + 1
                print(f"Datos cargando: {counter}", end="\r")

        except Exception as error:
            print("Error, al escribir el archivo final xml", error)

        print(f"\nTotal datos: [{len(self.data_index_xml)}] escritos en el archivo: {name_file_xml}\n")
        self.name_file = ""

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self):
        cwd = os.getcwd()
        list_files = os.listdir(cwd)
        self.files = [x for x in list_files if '.csv' in x or '.xml' in x]

        return self.files

    # Método para cargar los datos csv y xml
    def get_data_csv_and_xml(self):
        files_name = self.get_the_current_working_directory()
        print_files = [print(f"{[files_name.index(x)]}-{x}") for x in files_name]
        try:
            file_csv = int(input("Selecciona el archivo csv: "))
            file_xml = int(input("Selecciona el archivo xml: "))
            if ".csv" in files_name[file_csv] and ".xml" in files_name[file_xml]:
                self.get_csv_data_list(files_name[file_csv])
                self.xml_data_list(files_name[file_xml])
                self.name_file = files_name[file_xml]
            else:
                print("seleccionaste mal los archivos, debe ser 1 el csv y 2 el xml\n")
        except IndexError as error_index:
            print(f"Error: {error_index} \n")

    # Método que imprime el menu que tiene el sistema
    def menu(self):
        while self.flag:
            print('[1]Cargar datos csv y xml')
            print('[2]Buscar datos en estados de cuenta')
            print('[3]Escribir archivo final')
            print('[0]Salir')
            commad = str(input('Que deseas hacer \n$:'))
            if commad == '1':
                self.get_data_csv_and_xml()
            elif commad == '2':
                self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
            elif commad == '3':
                self.write_file_xml()
                self.build_xml(self.name_file, self.name_file_xml, self.data_index_xml)
            elif commad == '0':
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
        print("Descripción: Buscador de datos xml\n")
        print("positional arguments:")
        print(" main.py file.csv file.xml Name-file.xml\n")
        print("optional arguments:")
        print(" -h, --help  show this help message and exit")

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, argv):
        print(f"Archivos agregados: CSV: {argv[1]} XML: {argv[2]} Name-file: {argv[3]}")
        self.get_csv_data_list(argv[1])
        self.xml_data_list(argv[2])
        self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
        self.build_xml(argv[2], argv[3], self.data_index_xml)
