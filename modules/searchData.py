import csv 
import os

class Data:

    def __init__(self):
        self.data_array_xml = []
        self.final_data = []
        self.data_array_csv = []
        self.files = []
        self.flag = True
        self.reading_method = 'r'
        self.write_method = 'w'
        self.name_file = ''
        self.count = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
    #metodo encargado de escribir los archivos en el sistema
    def write_file(self, final_data):
        self.name_file = str(input(f"nombre del archivo\n:"))
        self.final_data = ' '.join(map(str, self.final_data))
        try:
            with open(self.name_file, self.write_method) as write_file:
                write_file.write(self.final_data)
            print(f"Se acredo el archivo {self.name_file}, con sus datos")
        except:
            print('no se pudo escribrir el archivo')
    #metodo encargado de leer los datos que están en el archivo csv
    def csv_data_list(self, name_file):
        try:
            with open(self.name_file, self.reading_method) as (File):
                reader = csv.reader(File)
                for row in reader:
                    data_clean = ''.join(row)
                    self.data_array_csv.append(data_clean)

            print(f"\nTotal: {len(self.data_array_csv)} datos\n")
        except Exception as e:
            print('no se pudo cargar los datos del csv', e)

        return self.data_array_csv
    #metodo encargado de leer el archivo xml
    def xml_data_list(self, name_file):
        try:
            with open(self.name_file, self.reading_method) as (data_xml):
                extracted_data = data_xml.readlines()
                max_lend_xml = len(extracted_data)
                for i in range(max_lend_xml):
                    data_with_new_line = extracted_data[i].rstrip('\n')
                    self.data_array_xml.append(data_with_new_line)

            print(f"\nTotal lineas xml: {len(self.data_array_xml)}\n")
        except:
            print('no se pudo obtener datos')
    #metodo encargado de consultar y armar todos los datos del xml
    def search_data_xml(self, data_array_xml, data_array_csv):
        try:
            self.final_data.insert(0, self.data_array_xml[0])
            self.final_data.insert(1, self.data_array_xml[1])
        except:
            print('verifica que los datos xml esten cargado en el sistema')

        max_index_data = len(self.data_array_xml) - 1
        while self.count <= max_index_data:
            self.flag = True
            only_one_data = self.data_array_xml[self.count]
            obligation = '<OBLIGACION>' in only_one_data
            try:
                if obligation == True:
                    self.count2 = self.count + 2
                    account_status = self.data_array_csv[self.count3] in self.data_array_xml[self.count2]
                    if account_status == True:
                        while self.flag:
                            self.final_data.append(only_one_data)
                            self.count = self.count + 1
                            obligation_end = '</OBLIGACION>' in self.data_array_xml[self.count]
                            only_one_data = self.data_array_xml[self.count]
                            if obligation_end == True:
                                self.final_data.append(only_one_data)
                                self.count2 = 0
                                self.flag = False
                                self.data_array_csv.pop(0)
                                self.count = 0
                                self.count4 = self.count4 + 1
                                continue

                max_index_data_csv = len(self.data_array_csv)
                if max_index_data_csv == 0:
                    self.flag = True
                    self.final_data.append(self.data_array_xml[(-1)])
                    print(f"\nTotal datos xml: {self.count4}\n")
                    self.count4 = 0
                    self.data_array_xml.clear()
                    break
            except Exception as error:
                print('error:', error)

            self.count = self.count + 1
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
    #methodo que imprime el menu que tiene el sistema
    def menu(self):
        while self.flag:
            print('[1]seleccionar archivo')
            print('[2]cargar datos csv')
            print('[3]cargar datos xml')
            print('[4]buscar datos estados de cuenta')
            print('[5]escribir archivo')
            print('[0]salir')
            commad = str(input('Que deseas hacer \n$:'))
            if commad == '1':
                self.send_data_in_list()
            elif commad == '2':
                self.csv_data_list(self.name_file)
            elif commad == '3':
                self.xml_data_list(self.name_file)
            elif commad == '4':
                self.search_data_xml(self.data_array_xml, self.data_array_csv)
            elif commad == '5':
                self.write_file(self.final_data)
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

# datos = Csv('mediano.csv')
# reultado = datos.datos_in_list()