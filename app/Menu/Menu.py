from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
from Config import Messages, Config
import os
import traceback


class Menu:
    """
    Está clase fue diseñada para poder mostrar al usuario un menú para utilizar la aplicación,
    o poder ejecutar la aplicación por medio de argumentos que recibe la aplicación.

    Attributes:
    ----------
        _flag (bool): Esté atributo se utiliza para poder ejecutar el menú que tiene la aplicación.
        csv (class): Esté atributo se utiliza para poder instaciar la clase Csv y poder invocar los métodos.
        xml (class): Esté atributo se utiliza para poder instancia la clase Xml y poder invocar los métodos.
        messages (class): Esté atributo se utiliza para poder instancia la clase Messages y poder invocar los métodos.
        BASE_DIR (class): Esté atributo se utiliza para poder instancia la clase Config y importar la ruta raíz del proyecto.

    Methods:
    -------
        menu() -> None:
        get_data_csv_and_xml() -> dict
        filter_directory_by_xml_and_csv_files() -> list
        build_xml_with_arguments(arg_list: list) -> None
        format_xml_with_arguments(arg_list: list) -> None
        export_data_csv_arguments(arg_list: list) -> None
        def export_csv_data_united(arg_list: list) -> None:
        exporting_multiple_csv_files(arg_list: list) -> None:
        merge_csv_files(arg_list: list) -> None:
        lists_of_data_to_compare(arg_list: list) -> None:
        remove_xml_values_with_arguments(arg_list: list) -> None
        print_random_days(arg_list: list) -> None
        identify_system() -> None
        print_message() -> None
        print_message_help() -> None
    """
    def __init__(self):
        """ El constructor de la clase Menu
        """
        self._flag: bool = True
        self.csv = Csv()
        self.xml = Xml()
        self.messages = Messages()
        self.BASE_DIR = Config().BASE_DIR
        self.PATH_DIR = Config()

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
                total_data = self.xml.build_xml(xml_file_name=get_data['chosen_xml_file'], name_of_the_new_xml_file=name_of_the_chosen_xml, data_index_xml=data_index_xml)
                print(f'Total datos copiados: {total_data}')
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

            filter_directory_by_xml_and_csv_files() Trae los nombres de los archivos XML y CSV,
            get_csv_data_list() Trae una lista con datos del archivo CSV,
            get_xml_data_list() Trae una lista con datos del archivo XML.
        """
        files_name = self.filter_directory_by_xml_and_csv_files()
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
            print(f"uncaught exception {traceback.format_exc()}")
            print(self.messages.print_message_yellow(message="Posible error: selecciono mal los archivos"))
            print(self.messages.print_error(programmer_error_message="Error al intentar seleccionar los archivos", error_message_from_method=error_index))

    # Método encargado de obtener el directorio de trabajo donde esta el proyecto y sus archivos
    def filter_directory_by_xml_and_csv_files(self) -> list:
        """ Este método se diseñó para poder leer los archivos que están en el directorio,
            y poder filtrarlos por archivos XML y CSV

        Returns:
            list: Una lista con los nombres de los archivos CSV y XML.
        """
        cwd = os.getcwd()
        file_list_in_directory = self.PATH_DIR.get_the_current_working_directory(path_dir=cwd)
        files_list = [item for item in file_list_in_directory if '.csv' in item or '.xml' in item]
        return files_list

    # Método para construir el archivo por medio de argumentos por linea de comando
    def build_xml_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para construir los archivos XML por medio de la terminal con argumentos,
            que recibe la aplicación.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos CSV y XML,
            que se agregaron por argumentos de la aplicación.
        """
        print(self.messages.print_message_blue(message="Archivos agregados:"))
        print(f"* CSV: {self.messages.print_message_yellow(message=arg_list[1])}")
        print(f"* XML: {self.messages.print_message_green(message=arg_list[2])}")
        print(f"* Name of the new xml file: {self.messages.print_message_magenta(message=arg_list[3])}\n")
        csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[1])
        total_list_csv = len(csv_list)
        print(f'{self.messages.print_message_blue(message="Total datos en archivo csv:")} {self.messages.print_message_yellow(message=str(total_list_csv))}')
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[2])
        total_list_xml = len(xml_list)
        print(f'{self.messages.print_message_blue(message="Total datos en archivo xml:")} {self.messages.print_message_yellow(message=str(total_list_xml))}')
        xml_index = self.xml.search_the_index_in_the_list(data_list_csv=csv_list, data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print(f'{self.messages.print_message_blue(message="Total indexes encontrados:")} {self.messages.print_message_yellow(message=str(total_list_index))}')
        total_data = self.xml.build_xml(xml_file_name=arg_list[2], name_of_the_new_xml_file=arg_list[3], data_index_xml=xml_index)
        print(f'{self.messages.print_message_blue(message="Total datos copiados:")} {self.messages.print_message_yellow(message=str(total_data))}')

    # Método para formatear archivos xml por medio de argumentos por linea de comando
    def format_xml_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder verificar si el archivo XML está formateado,
            si no está formateado le dará un formato para poder leer los datos y si es lo contrario,
            no hará nada.
        Args:
            arg_list (list): Recibe una lista con el nombre del archivo xml y poder dar formato.
        """
        print(self.messages.print_message_blue(message="Archivo agregado para formatear:"))
        print(f"* XML: {self.messages.print_message_green(message=arg_list[2])}")
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            el archivo XML que se esté trabajando y poder exportarlos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos XML y CSV.
        """
        print(self.messages.print_message_blue(message="Archivos agregados:"))
        print(f"* XML: {self.messages.print_message_yellow(message=arg_list[2])}")
        print(f"* CSV: {self.messages.print_message_green(message=arg_list[3])}\n")
        self.xml.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[2])
        print(f'{self.messages.print_message_blue(message="Total estados de cuenta xml:")} {self.messages.print_message_yellow(message=str(len(xml_list)))}')
        self.csv.export_data_csv(data_list_xml=xml_list, csv_file_name=arg_list[3])

    def export_csv_data_united(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV.
        """
        dictionary_with_data = self.xml.export_all_multiple_data_xml(path_of_archives=arg_list[2])
        data_list = []
        for item_xml in dictionary_with_data:
            data_list.extend(dictionary_with_data[item_xml])

        self.csv.export_data_csv(data_list_xml=data_list, csv_file_name=arg_list[3])
        print(f'{self.messages.print_message_blue(message="Total estados:")} {self.messages.print_message_yellow(message=str(len(data_list)))}')


    def exporting_multiple_csv_files(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a varios archivos CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio.
        """
        dictionary_with_data = self.xml.export_all_multiple_data_xml(path_of_archives=arg_list[2])
        for item_xml in dictionary_with_data:
            self.csv.export_data_csv(data_list_xml=dictionary_with_data[item_xml], csv_file_name=f"{item_xml}.csv")
            length_data = len(dictionary_with_data[item_xml])
            print(f'{self.messages.print_message_blue(message=f"Archivo Exportado:{item_xml}.csv")} {self.messages.print_message_yellow(message=str(length_data))}')

    def merge_csv_files(self, arg_list: list) -> None:
        """ Este método se diseñó para unir todo los archivos CSV que se encuentren en el direcotrio,
            que le indiquen y exportara un solo archivo CSV con todos los datos.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV,
            que va a almacenar los datos.
        """
        file_list_in_directory = self.PATH_DIR.get_the_current_working_directory(path_dir=arg_list[2])
        csv_file_list = [value for value in file_list_in_directory if ".csv" in value]

        join_data = []
        for item_csv in csv_file_list:
            print(item_csv)
            csv_list = self.csv.get_csv_data_list(csv_file_name=item_csv)
            join_data.extend(csv_list)
            # for item in csv_list:
            #     join_data.append(item)

        print(len(join_data))
        self.csv.export_data_csv(data_list_xml=join_data, csv_file_name=arg_list[3])

    def lists_of_data_to_compare(self, arg_list: list) -> None:
        """ Este método se diseñó para comparar dos listas de datos y exportar un archivo CSV,
            con los datos filtrados.

        Args:
            arg_list (list): Recibe dos listas con los datos que se van a comparar y el nombre,
            del archivo que se va a exportar
        """
        print(self.messages.print_message_blue(message="Archivos agregados:"))
        print(f"* CSV-MASTER: {self.messages.print_message_green(message=arg_list[2])}")
        print(f"* CSV-compare: {self.messages.print_message_yellow(message=arg_list[3])}\n")
        csv_list_master = self.csv.get_csv_data_list(csv_file_name=arg_list[3])
        print(len(csv_list_master))
        csv_list_two = self.csv.get_csv_data_list(csv_file_name=arg_list[2])
        print(len(csv_list_two))
        no_iguales = self.csv.compare_lists_of_data(master_list=csv_list_master, data_list_two=csv_list_two)
        print(len(no_iguales))
        self.csv.export_data_csv(data_list_xml=no_iguales, csv_file_name="exporting-duplicates.csv")

    # Método para eliminar los estados de cuenta, por medio de argumentos por linea de comando
    def remove_xml_values_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder remover los estados de cuenta que se especifiquen,
            en el archivo csv y poder borrarlos del archivo xml.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos xml y csv
        """
        print(self.messages.print_message_blue(message="Archivos agregados:"))
        print(f"* CSV: {self.messages.print_message_green(message=arg_list[2])}")
        print(f"* XML: {self.messages.print_message_yellow(message=arg_list[3])}\n")
        csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[2])
        total_list_csv = len(csv_list)
        print(f'{self.messages.print_message_blue(message="Total datos csv a eliminar:")} {self.messages.print_message_yellow(message=str(total_list_csv))}')
        self.xml.check_and_format_xml(xml_file_name=arg_list[3])
        xml_list = self.xml.get_xml_data_list(xml_file_name=arg_list[3])
        total_list_xml = len(xml_list)
        print(f'{self.messages.print_message_blue(message="Total estados de cuenta xml:")} {self.messages.print_message_yellow(message=str(total_list_xml))}')
        xml_index = self.xml.search_the_index_in_the_list(data_list_csv=csv_list, data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print(f'{self.messages.print_message_blue(message="Total indexes encontrados que se van a eliminar")} {self.messages.print_message_yellow(message=str(total_list_index))}')
        total_data_removed = self.xml.remove_xml_values(xml_file_name=arg_list[3], data_index_xml=xml_index)
        print(f'{self.messages.print_message_green(message="Total datos eliminados:")} {self.messages.print_message_green(message=str(total_data_removed))}')

    def print_random_days(self, arg_list: list) -> None:
        """ Este método se diseñó para poder seleccionar alzar los días de mora.

        Args:
            arg_list (list): Recibe una lista con el nombre del archivo csv y el número de días a buscar.
        """
        try:
            print(self.messages.print_message_blue(message="Archivo agregado:"))
            print(f"* CSV: {self.messages.print_message_magenta(message=arg_list[2])}")
            iterations = int(arg_list[3])
            print(f"* Iterations: {self.messages.print_message_yellow(message=str(iterations))}\n")
            csv_list = self.csv.get_csv_data_list(csv_file_name=arg_list[2])
            print(f'{self.messages.print_message_blue(message="Total datos en archivo csv:")} {self.messages.print_message_yellow(message=str(len(csv_list)))}\n')
            self.csv.select_days(data_list_csv=csv_list, amount=iterations)
        except Exception as error_message_elect_print_random_days:
            print(f"uncaught exception {traceback.format_exc()}")
            print(self.messages.print_message_yellow(message="Posible error: puede ser que ingreso letras y no un número."))
            print(self.messages.print_error(programmer_error_message="Error al intentar imprimir los días al azar.", error_message_from_method=error_message_elect_print_random_days))

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
    def print_message_help(self) -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de ayuda para el usuario y poder,
            ejecutar correctamente la aplicación.
        """
        try:
            path_messages = os.path.join(self.BASE_DIR, 'docs/messages/messages-help.txt')
            with open(path_messages, 'r') as file_with_help_messages:
                help_massages = file_with_help_messages.read()
                print(help_massages)
        except FileNotFoundError as error_help_file:
            print(self.messages.print_message_red(message="El archivo para imprimir las ayudas no se encuentra"))
            print(self.messages.print_message_yellow(message=f"{error_help_file.args[1]} {error_help_file.filename}"))
            print(self.messages.print_message_yellow(message="La ubicación del archivo: docs/messages/messages-help.txt"))
