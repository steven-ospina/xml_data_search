from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
import os


class Menu:
    """
    Está clase fue diseñada para poder mostrar al usuario un menú para utilizar la aplicación,
    o poder ejecutar la aplicación por medio de argumentos que recibe la aplicación.

    Attributes:
    ----------
        _flag (bool): Esté atributo se utiliza para poder ejecutar el menú que tiene la aplicación.
        csv (class): Esté atributo se utiliza para poder instaciar la clase Csv y poder invocar los métodos.
        xml (class): Esté atributo se utiliza para poder instancia la clase Xml y poder invocar los métodos.

    Methods:
    -------
        menu() -> None:
        get_data_csv_and_xml() -> dict:
        get_the_current_working_directory() -> list:
        build_xml_with_arguments(arg_list: list) -> None:
        format_xml_with_arguments(arg_list: list) -> None:
        export_data_csv_arguments(arg_list: list) -> None:
        remove_xml_values_with_arguments(arg_list: list) -> None
        def print_random_days(self, arg_list: list) -> None:
        identify_system() -> None:
        print_message() -> None:
        print_message_help() -> None:
    """
    def __init__(self):
        """ El constructor de la clase Menu
        """
        self._flag: bool = True
        self.csv = Csv()
        self.xml = Xml()

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
                get_data = self.get_data_csv_and_xml()
            elif command == '2':
                data_index_xml = self.xml.search_the_index_in_the_list(data_list_csv=get_data['csv_list'], data_list_xml=get_data['xml_list'])
                print(f"\nTotal indexes encontrados: {len(data_index_xml)}\n")
            elif command == '3':
                name_of_the_chosen_xml: str = self.xml.write_file_xml()
                self.xml.build_xml(xml_file_name=get_data['chosen_xml_file'], name_of_the_new_xml_file=name_of_the_chosen_xml, data_index_xml=data_index_xml)
            elif command == '0':
                self.identify_system()
                self._flag = False
            else:
                self.identify_system()
                self._flag = False

    # Método para cargar los datos csv y xml
    def get_data_csv_and_xml(self) -> dict:
        """ Este método se diseñó para poder seleccionar los archivos con lo que se va a trabajar,
            y poder invocar los metodos:

            get_the_current_working_directory() Trae los nombres de los archivos xml y csv,
            get_csv_data_list() Trae una lista con datos del archivo csv,
            get_csv_data_list() Trae una lista con datos del archivo xml.
        """
        files_name = self.get_the_current_working_directory()
        [print(f"{[files_name.index(item)]}-{item}") for item in files_name]
        try:
            csv_file = int(input("Selecciona el archivo csv: "))
            xml_file = int(input("Selecciona el archivo xml: "))
            if ".csv" in files_name[csv_file] and ".xml" in files_name[xml_file]:
                self.xml.check_and_format_xml(xml_file_name=files_name[xml_file])
                csv_list = self.csv.get_csv_data_list(csv_file_name=files_name[csv_file])
                print(f"\nTotal datos csv: {len(csv_list)}\n")
                xml_list = self.xml.get_xml_data_list(xml_file_name=files_name[xml_file])
                print(f"\nTotal estados de cuenta xml: {len(xml_list)}")

                data = {
                    "csv_list": csv_list,
                    "xml_list": xml_list,
                    "chosen_xml_file": files_name[xml_file]
                }
                return data
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
        file_list_in_directory = os.listdir(cwd)
        files_list = [item for item in file_list_in_directory if '.csv' in item or '.xml' in item]
        return files_list

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para construir los archivos xml por medio de argumentos,
            que recibe la aplicación.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos csv y xml,
                              que se agregaron por argumentos de la aplicación.
        """
        print("Archivos agregados:")
        print(f" * CSV: {arg_list[1]}")
        print(f" * XML: {arg_list[2]}")
        print(f" * Name-file: {arg_list[3]}")
        csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[1])
        print(f"\nTotal datos csv: {len(csv_list)}\n")
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[2])
        print(f"\nTotal estados de cuenta xml: {len(xml_list)}")
        xml_index = self.xml.search_the_index_in_the_list(data_list_csv=csv_list, data_list_xml=xml_list)
        print(f"\nTotal indexes encontrados: {len(xml_index)}\n")
        self.xml.build_xml(xml_file_name=arg_list[2], name_of_the_new_xml_file=arg_list[3], data_index_xml=xml_index)

    # Método para formatear archivos xml por medio de argumentos por linea de comando
    def format_xml_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder verificar si el archivo xml está formateado,
            si no está formateado le dará un formato para poder leer los datos y si es lo contrario,
            no hará nada.
        Args:
            arg_list (list): Recibe una lista con el nombre del archivo xml y poder dar formato.
        """
        print("Archivo agregado para formatear:")
        print(f" * XML: {arg_list[2]}")
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            el archivo xml que se esté trabajando y poder exportarlos a un archivo csv.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos xml y csv.
        """
        print("Archivos agregados:")
        print(f" * XML: {arg_list[2]}")
        print(f" * CSV: {arg_list[3]}")
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[2])
        print(f"\nTotal estados de cuenta xml: {len(xml_list)}")
        self.csv.export_data_csv(data_list_xml=xml_list, csv_file_name=arg_list[3])

    # Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
    def remove_xml_values_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder remover los estados de cuenta que se especifiquen,
            en el archivo csv y poder borrarlos del archivo xml.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos xml y csv
        """
        print("Archivos agregados:")
        print(f" * CSV: {arg_list[2]}")
        print(f" * XML: {arg_list[3]}")
        csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[2])
        print(f"\nTotal datos csv: {len(csv_list)}\n")
        self.xml.check_and_format_xml(xml_file_name=arg_list[3])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[3])
        print(f"\nTotal estados de cuenta xml: {len(xml_list)}")
        xml_index = self.xml.search_the_index_in_the_list(data_list_csv=csv_list, data_list_xml=xml_list)
        print(f"\nTotal indexes encontrados: {len(xml_index)}\n")
        self.xml.remove_xml_values(xml_file_name=arg_list[3], data_index_xml=xml_index)

    def print_random_days(self, arg_list: list) -> None:
        """ Este método se diseñó para poder seleccionar alzar los días de mora.

        Args:
            arg_list (list): Recibe una lista con el nombre del archivo csv y el número de días a buscar.
        """
        print("Archivo agregado:")
        print(f" * CSV: {arg_list[2]}")
        csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[2])
        print(f"\nTotal datos csv: {len(csv_list)}\n")
        iterations = int(arg_list[3])
        self.csv.select_days(data_list_csv=csv_list, amount=iterations)

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
        try:
            path = 'docs/messages/messages-help.txt'
            with open(path, 'r') as file_with_help_messages:
                help_massages = file_with_help_messages.read()
                print(help_massages)
        except FileNotFoundError as error:
            print(f"No se pudo imprimir los mesajes de ayudas, ERROR: {error}")
