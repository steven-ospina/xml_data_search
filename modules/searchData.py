import xml.etree.ElementTree as ET
import csv, os 
from copy import deepcopy

class Data:

    def __init__(self, name_file = "", name_file_xml = ""):
        self.data_array_xml = []
        self.data_array_csv = []
        self.data_index_xml = []
        self.files = []
        self.flag = True
        self.reading_method = 'r'
        self.write_method = 'w'
        self.name_file = name_file
        self.name_file_xml = name_file_xml

    #metodo encargado de escribir los archivos en el sistema
    def write_file_xml(self):
        print("recuerda poner al final del nombre la extension *.xml")
        self.name_file_xml = str(input(f"nombre del archivo\n:"))
        try:
            respuesta = str(input(f"El nombre del archivo es: {self.name_file_xml} \n [si] o [no]\n:"))
            if respuesta.lower() == 'si':
                self.name_file_xml = self.name_file_xml
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error:
            print('Error: ', error)

        return self.name_file_xml
    #metodo encargado de leer los datos que están en el archivo csv
    def csv_data_list(self,name_file):

        try:
            with open(self.name_file, self.reading_method) as (File):
                reader = csv.reader(File)
                for row in reader:
                    data_clean = ''.join(row)
                    self.data_array_csv.append(data_clean)

            print(f"\nTotal: {len(self.data_array_csv)} datos\n")
        except Exception as e:
            print('no se pudo cargar los datos del csv', e)
        
        self.name_file = "" 

        return self.data_array_csv

    #metodo para buscar los todos los numeros en el xml a consular
    def xml_data_list(self, name_file):

        root = ET.parse(self.name_file).getroot()

        for child in root.findall(f"./OBLIGACION/ENCABEZADO"):
            estado = child.find('ESTADOCUENTA').text
            self.data_array_xml.append(estado)

        print(f"\nTotal estados de cuenta xml: {len(self.data_array_xml)}\n")

        return self.data_array_xml

    #metodo encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self):
        max_lent_search = len(self.data_array_csv)

        try:

            for i in range(max_lent_search):
                data_only = self.data_array_csv[i]
                index_list = self.data_array_xml.index(data_only)
                self.data_index_xml.append(index_list)

            print(f"\nTotal datos: {len(self.data_index_xml)}\n")

        except Exception as error:
            print("error: ", error) 

        return self.data_index_xml


    # #metodo encargado de consultar y armar todos los datos del xml
    def build_xml(self,name_file, name_file_xml):
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.dump(ESTADODECUENTA)
            root_fie_new = ET.ElementTree(ESTADODECUENTA).write(self.name_file_xml, encoding="UTF-8", xml_declaration=True)

            root_source_file = ET.parse(self.name_file).getroot()
            tree = ET.parse(self.name_file_xml).getroot()

            for i in self.data_index_xml:
                obligacion_source_file = root_source_file[i]

                obligacion_copy = deepcopy(obligacion_source_file)

                tree.append(obligacion_copy)

                root_fie_new = ET.ElementTree(tree).write(self.name_file_xml, encoding="UTF-8", xml_declaration=True)
        except Exception as error:
            print("error al escribir el archivo", error)

        print(f"\nTotal datos: {len(self.data_array_xml)}\n")
        self.name_file = ""

    #metodo encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self):
        cwd = os.getcwd()
        self.files = os.listdir(cwd)
        key = len(self.files)
        for key in range(key):
            print(f"[{key}]-{self.files[key]}")

        return self.files

    #metodo encargado de seleccionar el archivo a trabajar
    def send_data_in_list(self):
        self.get_the_current_working_directory()
        try:
            selected = int(input('Selecciona el archivo:'))
            respuesta = str(input(f"El nombre del archivo es: {self.files[selected]} \n [si] o [no]\n:"))
            if respuesta.lower() == 'si':
                self.name_file = self.files[selected]
            else:
                print('Busca el archivo correcto\n')
        except ValueError as error:
            print('no es un numero,', error)

        return self.name_file

    #methodo que imprime el menu que tiene el sistema
    def menu(self):
        while self.flag:
            print('[1]cargar datos csv')
            print('[2]cargar datos xml')
            print('[3]buscar datos estados de cuenta')
            print('[4]escribir archivo')
            print('[0]salir')
            commad = str(input('Que deseas hacer \n$:'))
            if commad == '1':
                self.send_data_in_list()
                self.csv_data_list(self.name_file)
            elif commad == '2':
                self.send_data_in_list()
                self.xml_data_list(self.name_file)
            elif commad == '3':
                # self.search_data_xml(self.data_array_xml, self.data_array_csv)
                self.search_the_index_in_the_list()
            elif commad == '4':
                self.write_file_xml()
                self.build_xml(self.name_file, self.name_file_xml)
            elif commad == '0':
                self.indetificar_sistema()
                self.flag = False
            else:
                self.indetificar_sistema()
                self.flag = False

    #metodo para identificar el sistema operativo para poder limpiar la consola
    def indetificar_sistema(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')

    #metodo para imprimir mensaje de inicio del scrip
    def print_message(self):
        print('B I E N V E N I D O\n')
        print('Nota: verifica que en directorio del proyecto estén los archivos:')
        print('[*.csv y *.xml]')
        print('[Los datos del csv deben estar en una sola columna y solo numeros]')
        print('[cargar un archivo csv y xml a la ves]\n')
