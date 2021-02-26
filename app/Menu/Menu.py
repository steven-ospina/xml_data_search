from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
import os


class Menu:
    """
    Está clase fue diseñada para poder mostrar al usuario un menú para utilizar la aplicación,
    o poder ejecutar la aplicación por medio de argumentos que recibe la aplicación.

    Attributes:
        _flag (bool): Esté atributo se utiliza para poder ejecutar el menú que tiene la aplicación.
        name_file (string): Esté atributo se utiliza para poder guardar los nombres de los archivos.
        csv (class): Esté atributo se utiliza para poder instaciar la clase Csv y poder invocar los métodos.
        xml (class): Esté atributo se utiliza para poder instancia la clase Xml y poder invocar los métodos.
        data_list_csv (list): Esté atributo se utiliza para poder guardar los los datos que retorna el método get_csv_data_list().
        data_list_xml (list): Esté atributo se utiliza para poder guardar los los datos que retorna el método get_xml_data_list().
        data_index_xml (list): Esté atributo se utiliza para poder guardar los los datos que retorna el método search_the_index_in_the_list().
        files (list): Esté atributo se utiliza para poder guardar la lista filtrada de los archivos xml y csv del directorio de trabajo.
    """
    def __init__(self):
        """ El constructor de la clase Menu
        """
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
        """ Este método se diseñó para cargar el menú que tiene la aplicación.
        """
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
        """ Este método se diseñó para poder seleccionar los archivos con lo que se va a trabajar,
            y poder invocar los metodos:

            get_the_current_working_directory() Trae los nombres de los archivos xml y csv,
            get_csv_data_list() Trae una lista con datos del archivo csv,
            get_csv_data_list() Trae una lista con datos del archivo xml.
        """
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
                print("Seleccionaste mal los archivos, debe ser 1 el csv y 2 el xml\n")
        except IndexError as error_index:
            print(f"Error: {error_index} \n")

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def get_the_current_working_directory(self) -> list:
        """ Este método se diseñó para poder leer los archivos que están en el directorio,
            y poder filtrarlos por archivos xml y csv

        Returns:
            list: Una lista con los nombres de los archivos csv y xml.
        """
        cwd = os.getcwd()
        list_files = os.listdir(cwd)
        self.files = [item for item in list_files if '.csv' in item or '.xml' in item]
        return self.files

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, argv_list: list) -> None:
        """ Este método se diseñó para construir los archivos xml por medio de argumentos,
            que recibe la aplicación.

        Args:
            argv_list (list): Recibe una lista con los nombres de los archivos csv y xml,
                              que se agregaron por argumentos de la aplicación.
        """
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
        """ Este método se diseñó para poder verificar si el archivo xml está formateado,
            si no está formateado le dará un formato para poder leer los datos y si es lo contrario,
            no hará nada.
        Args:
            argv_list (list): Recibe una lista con el nombre del archivo xml y poder dar formato.
        """
        print("Archivos agregado para formatear:")
        print(f" * XML: {argv_list[2]}")
        self.xml.check_and_format_xml(name_file_xml=argv_list[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, argv_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            el archivo xml que se esté trabajando y poder exportarlos a un archivo csv.

        Args:
            argv_list (list): Recibe una lista con los nombres de los archivos xml y csv.
        """
        print("Archivos agregados:")
        print(f" * XML: {argv_list[2]}")
        print(f" * CSV: {argv_list[3]}")
        self.xml.check_and_format_xml(name_file_xml=argv_list[2])
        self.data_list_xml = self.xml.get_xml_data_list(name_file=argv_list[2])
        self.csv.export_data_csv(data_list_xml=self.data_list_xml, name_file_csv=argv_list[3])

    # Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
    def remove_xml_values_with_arguments(self, argv_list: list) -> None:
        """ Este método se diseñó para poder remover los estados de cuenta que se especifiquen,
            en el archivo csv y poder borrarlos del archivo xml.

        Args:
            argv_list (list): Recibe una lista con los nombres de los archivos xml y csv
        """
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
        """ Este método se diseñó para poder identificar el sistema operativo donde se ejecuta la aplicación,
            y poder limpiar la consola cuando se termine de utilizar la aplicación por medio del menú.
        """
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')

    # Método que imprime el mensaje de inicio del script
    @staticmethod
    def print_message() -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de guía para el usuario al momento,
            de ejecutar la aplicación por el menú.
        """
        print('B I E N V E N I D O\n')
        print('Nota: verifica que en directorio del proyecto estén los archivos:')
        print('[*.csv y *.xml]')
        print('[Los datos del csv deben estar en una sola columna y solo números]')
        print('[Cargar un archivo csv y xml a la ves]\n')
        print('[El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]\n')

    # Método que imprime el mensaje de ayuda para el usuario
    @staticmethod
    def print_message_help() -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de ayuda para el usuario y poder,
            ejecutar correctamente la aplicación.
        """
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
