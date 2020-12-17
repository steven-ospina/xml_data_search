from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
import os


class Menu:
    def __init__(self):
        self._flag: bool = True
        self.name_file: str = ""
        self.csv = Csv()
        self.xml = Xml()
        self.data_list_csv: list = []
        self.data_list_xml: list = []
        self.data_index_xml: list = []
        self.files: list = []

        # Método que imprime el menu que tiene el sistema
    def menu(self) -> None:
        while self._flag:
            print('[1]Cargar datos csv y xml')
            print('[2]Buscar datos en estados de cuenta')
            print('[3]Escribir archivo final')
            print('[0]Salir')
            command = str(input('Que deseas hacer \n$:'))
            if command == '1':
                self.get_data_csv_and_xml()
            elif command == '2':
                self.data_index_xml = self.xml.search_the_index_in_the_list(data_list_csv=self.data_list_csv, data_list_xml=self.data_list_xml)
            elif command == '3':
                name_file_xml: str = self.xml.write_file_xml()
                self.xml.build_xml(name_file=self.name_file, name_file_xml=name_file_xml, data_index_xml=self.data_index_xml)
            elif command == '0':
                self.identify_system()
                self._flag = False
            else:
                self.identify_system()
                self._flag = False

    # Método para cargar los datos csv y xml
    def get_data_csv_and_xml(self) -> None:
        files_name = self.get_the_current_working_directory()
        [print(f"{[files_name.index(item)]}-{item}") for item in files_name]
        try:
            file_csv = int(input("Selecciona el archivo csv: "))
            file_xml = int(input("Selecciona el archivo xml: "))
            if ".csv" in files_name[file_csv] and ".xml" in files_name[file_xml]:
                self.xml.check_and_format_xml(name_file_xml=files_name[file_xml])
                self.data_list_csv = self.csv.get_csv_data_list(name_file=files_name[file_csv])
                self.data_list_xml = self.xml.get_xml_data_list(name_file=files_name[file_xml])
                self.name_file = files_name[file_xml]
            else:
                print("seleccionaste mal los archivos, debe ser 1 el csv y 2 el xml\n")
        except IndexError as error_index:
            print(f"Error: {error_index} \n")

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self) -> list:
        cwd = os.getcwd()
        list_files = os.listdir(cwd)
        self.files = [item for item in list_files if '.csv' in item or '.xml' in item]
        return self.files

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, argv_list: list) -> None:
        print("Archivos agregados:")
        print(f" * CSV: {argv_list[1]}")
        print(f" * XML: {argv_list[2]}")
        print(f" * Name-file: {argv_list[3]}")
        self.data_list_csv = self.csv.get_csv_data_list(name_file=argv_list[1])
        self.xml.check_and_format_xml(name_file_xml=argv_list[2])
        self.data_list_xml = self.xml.get_xml_data_list(name_file=argv_list[2])
        self.data_index_xml = self.xml.search_the_index_in_the_list(data_list_csv=self.data_list_csv, data_list_xml=self.data_list_xml)
        self.xml.build_xml(name_file=argv_list[2], name_file_xml=argv_list[3], data_index_xml=self.data_index_xml)

    # Método para formatear archivos xml por medio de argumentos por linea de comando
    def format_xml_with_arguments(self, argv_list: list) -> None:
        print("Archivos agregado para formatear:")
        print(f" * XML: {argv_list[2]}")
        self.xml.check_and_format_xml(name_file_xml=argv_list[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, argv_list: list) -> None:
        print("Archivos agregados:")
        print(f" * XML: {argv_list[2]}")
        print(f" * CSV: {argv_list[3]}")
        self.xml.check_and_format_xml(name_file_xml=argv_list[2])
        self.data_list_xml = self.xml.get_xml_data_list(name_file=argv_list[2])
        self.csv.export_data_csv(data_list_xml=self.data_list_xml, name_file_csv=argv_list[3])

    # Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
    def remove_xml_values_with_arguments(self, argv_list: list) -> None:
        print("Archivos agregados:")
        print(f" * CSV: {argv_list[2]}")
        print(f" * XML: {argv_list[3]}")
        self.data_list_csv = self.csv.get_csv_data_list(name_file=argv_list[2])
        self.xml.check_and_format_xml(name_file_xml=argv_list[3])
        self.data_list_xml = self.xml.get_xml_data_list(name_file=argv_list[3])
        self.data_index_xml = self.xml.search_the_index_in_the_list(data_list_csv=self.data_list_csv, data_list_xml=self.data_list_xml)
        self.xml.remove_xml_values(name_file=argv_list[3], data_index_xml=self.data_index_xml)

    # Método para identificar el sistema operativo para poder limpiar la consola
    @staticmethod
    def identify_system() -> None:
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')

    # Método que imprime el mensaje de inicio del script
    @staticmethod
    def print_message() -> None:
        print('B I E N V E N I D O\n')
        print('Nota: verifica que en directorio del proyecto estén los archivos:')
        print('[*.csv y *.xml]')
        print('[Los datos del csv deben estar en una sola columna y solo números]')
        print('[Cargar un archivo csv y xml a la ves]\n')
        print('[El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]\n')

    # Método que imprime el mensaje de ayuda para el usuario
    @staticmethod
    def print_message_help() -> None:
        print("Descripción: \n Buscador de datos xml, \n Formateado de xml, \n Exportador a csv, \n Eliminador de datos en el xml\n")
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
