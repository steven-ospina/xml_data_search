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
    def csv_data_list(self, name_file):
        self.name_file = name_file
        try:
            with open(self.name_file, self.reading_method) as (File):
                reader = csv.reader(File)
                self.data_array_csv = [''.join(x) for x in reader]
                print(f"\nTotal datos csv: {len(self.data_array_csv)}\n")
        except Exception as error:
            print('No se pudo cargar los datos del csv', error)

        self.name_file = ""

        return self.data_array_csv.sort()

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def xml_data_list(self, name_file):
        self.name_file = name_file
        root = ET.parse(self.name_file).getroot()
        self.data_array_xml = [x.find('ESTADOCUENTA').text for x in root.findall(f"./OBLIGACION/ENCABEZADO")]
        print(f"\nTotal estados de cuenta xml: {len(self.data_array_xml)}\n")

        return self.data_array_xml

    # Método encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self, data_array_csv, data_array_xml):
        try:
            self.data_array_csv = data_array_csv
            self.data_array_xml = data_array_xml
            self.data_index_xml = [self.data_array_xml.index(x) for x in self.data_array_csv]
            print(f"\nTotal datos encontrados: {len(self.data_index_xml)}\n")
        except Exception as error:
            print("Error, al buscar el index en el xml: ", error)

        return self.data_index_xml

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, name_file, name_file_xml, data_index_xml):
        self.name_file = name_file
        self.name_file_xml = name_file_xml
        self.data_index_xml = data_index_xml
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.dump(ESTADODECUENTA)
            root_fie_new = ET.ElementTree(ESTADODECUENTA).write(self.name_file_xml, encoding="UTF-8", xml_declaration=True)
            root_source_file = ET.parse(self.name_file).getroot()
            tree = ET.parse(self.name_file_xml).getroot()
            # tree = [deepcopy(root_source_file[x]) for x in self.data_index_xml]
            for i in self.data_index_xml:
                obligacion_source_file = root_source_file[i]
                obligacion_copy = deepcopy(obligacion_source_file)
                tree.append(obligacion_copy)
                root_fie_new = ET.ElementTree(tree).write(self.name_file_xml, encoding="UTF-8", xml_declaration=True)

        except Exception as error:
            print("Error, al escribir el archivo final xml", error)

        print(f"\nTotal datos: [{len(self.data_index_xml)}] escritos en el archivo: {self.name_file_xml}\n")
        self.name_file = ""

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self):
        cwd = os.getcwd()
        self.files = os.listdir(cwd)
        working_directories = [print(f"{[self.files.index(x)]}-{x}") for x in self.files]

        return self.files

    # Método encargado de seleccionar el archivo a trabajar
    def send_data_in_list(self):
        self.get_the_current_working_directory()
        try:
            selected = int(input('Selecciona el archivo:'))
            answer = str(input(f"El nombre del archivo es: {self.files[selected]} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                self.name_file = self.files[selected]
            else:
                print('Busca el archivo correcto\n')
        except Exception as error:
            print('Error: ', error)

        return self.name_file

    # Método que imprime el menu que tiene el sistema
    def menu(self):
        while self.flag:
            print('[1]Cargar datos csv')
            print('[2]Cargar datos xml')
            print('[3]Buscar datos en estados de cuenta')
            print('[4]Escribir archivo final')
            print('[0]Salir')
            commad = str(input('Que deseas hacer \n$:'))
            if commad == '1':
                self.send_data_in_list()
                self.csv_data_list(self.name_file)
            elif commad == '2':
                self.send_data_in_list()
                self.xml_data_list(self.name_file)
            elif commad == '3':
                self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
            elif commad == '4':
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
        self.csv_data_list(argv[1])
        self.xml_data_list(argv[2])
        self.search_the_index_in_the_list(self.data_array_csv, self.data_array_xml)
        self.build_xml(argv[2], argv[3], self.data_index_xml)
