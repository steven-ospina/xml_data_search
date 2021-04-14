from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
from Config import Messages, Config
import os
import traceback
import re

messages = Messages()
config = Config()
xml = Xml()
csv = Csv()
basename = config.basename


class Menu:
    """
    Está clase fue diseñada para poder mostrar al usuario un menú para,
    utilizar la aplicación, o poder ejecutar la aplicación por medio de,
    argumentos que recibe la aplicación.

    Attributes:
    ----------
        _flag (bool): Esté atributo se utiliza para poder ejecutar el menú,
        que tiene la aplicación.

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
        self._flag: bool = True

    # Método que imprime el menu que tiene el sistema
    def menu(self) -> None:
        """ Este método se diseñó para cargar el menú que tiene la aplicación.
        """
        self.print_message()
        while self._flag:
            print('[1]Cargar datos csv y xml')
            print('[2]Buscar datos en estados de cuenta')
            print('[3]Escribir archivo final')
            print('[0]Salir')
            command = str(input('Que deseas hacer \n$:'))
            if command == '1':
                get_data = self.get_data_csv_and_xml()
            elif command == '2':
                data_index_xml = xml.search_the_index_in_the_list(
                    data_list_csv=get_data['csv_list'], data_list_xml=get_data['xml_list'])
                print(f"\nTotal indexes encontrados: {len(data_index_xml)}\n")
            elif command == '3':
                name_of_the_chosen_xml: str = xml.write_file_xml()
                total_data = xml.build_xml(
                    xml_file_name=get_data['chosen_xml_file'],
                    name_of_the_new_xml_file=name_of_the_chosen_xml,
                    data_index_xml=data_index_xml)
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
            y poder invocar los métodos:

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
                xml.check_and_format_xml(xml_file_name=files_name[xml_file])
                csv_list = csv.get_csv_data_list(csv_file_name=files_name[csv_file])
                print(f"\nTotal datos csv: {len(csv_list)}\n")
                xml_list = xml.get_xml_data_list(xml_file_name=files_name[xml_file])
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
            print(messages.print_messages_in_colors("Posible error: selecciono mal los archivos", color='yellow'))
            print(messages.print_error(
                programmer_error_message="Error al intentar seleccionar los archivos",
                error_message_from_method=error_index))

    @staticmethod
    def filter_directory_by_xml_and_csv_files() -> list:
        """ Este método se diseñó para poder leer los archivos que están en el directorio,
            y poder filtrarlos por archivos XML y CSV

        Returns:
            list: Una lista con los nombres de los archivos CSV y XML.
        """
        cwd = os.getcwd()
        file_list_in_directory = config.get_the_current_working_directory(path_dir=cwd)
        files_list = [item for item in file_list_in_directory if item.endswith('.csv') or item.endswith('.xml')]
        return files_list

    @staticmethod
    def build_xml_with_arguments(arg_list: list) -> None:
        """ Este método se diseñó para construir los archivos XML por medio de la terminal con argumentos,
            que recibe la aplicación.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos CSV y XML,
            que se agregaron por argumentos de la aplicación.
        """
        csv_file = arg_list[0]
        xml_file = arg_list[1]
        new_xml_file = arg_list[2]
        print(messages.print_messages_in_colors('Archivos agregados:', color='blue'))
        print(f"└──>CSV → {messages.print_messages_in_colors(basename(path_dir=csv_file), color='yellow')}")
        print(f"└──>XML → {messages.print_messages_in_colors(basename(path_dir=xml_file), color='green')}")
        print("└──>Name of the new xml file → "
              f"{messages.print_messages_in_colors(basename(path_dir=new_xml_file), color='magenta')}\n")
        csv_list = csv.get_csv_data_list(csv_file_name=csv_file)
        total_list_csv = len(csv_list)
        print_info_csv = messages.print_messages_in_colors(
            "Total datos en archivo csv:",
            str(total_list_csv), color1='blue', color2='yellow')
        print(print_info_csv[0], print_info_csv[1])
        xml.check_and_format_xml(xml_file_name=xml_file)
        xml_list = xml.get_xml_data_list(xml_file_name=xml_file)
        total_list_xml = len(xml_list)
        print_info_xml = messages.print_messages_in_colors(
            "Total datos en archivo xml:",
            str(total_list_xml), color1='blue', color2='yellow')
        print(print_info_xml[0], print_info_xml[1])
        xml_index = xml.search_the_index_in_the_list(
            data_list_csv=csv_list,
            data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print_info_index = messages.print_messages_in_colors(
            "Total indexes encontrados:",
            str(total_list_index), color1='blue', color2='yellow')
        print(print_info_index[0], print_info_index[1])
        total_data = xml.build_xml(
            xml_file_name=xml_file,
            name_of_the_new_xml_file=new_xml_file,
            data_index_xml=xml_index)
        print_info_copy = messages.print_messages_in_colors(
            "Total datos copiados:",
            str(total_data), color1='blue', color2='yellow')
        print(print_info_copy[0], print_info_copy[1])

    @staticmethod
    def format_xml_with_arguments(arg_list: list) -> None:
        """ Este método se diseñó para poder verificar si el archivo XML está formateado,
            si no está formateado le dará un formato para poder leer los datos y si es lo contrario,
            no hará nada.
        Args:
            arg_list (list): Recibe una lista con el nombre del archivo xml y poder dar formato.
        """
        xml_file = arg_list[0]
        print(messages.print_messages_in_colors("Archivo agregado para formatear:", color='blue'))
        print(f"└──>XML → {messages.print_messages_in_colors(basename(path_dir=xml_file), color='green')}")
        xml.check_and_format_xml(xml_file_name=xml_file)

    @staticmethod
    def export_data_csv_arguments(arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            el archivo XML que se esté trabajando y poder exportarlos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos XML y CSV.
        """
        xml_file = arg_list[0]
        csv_file = arg_list[1]
        print(messages.print_messages_in_colors("Archivos agregados:", color='blue'))
        print(f"└──>xml → {messages.print_messages_in_colors(basename(path_dir=csv_file), color='yellow')}")
        print(f"└──>CSV → {messages.print_messages_in_colors(basename(path_dir=xml_file), color='green')}")
        xml.check_and_format_xml(xml_file_name=xml_file)
        xml_list = xml.get_xml_data_list(xml_file_name=xml_file)
        print_info_xml = messages.print_messages_in_colors(
            "Total estados de cuenta xml: ",
            str(len(xml_list)), color1='blue', color2='yellow')
        print(print_info_xml[0], print_info_xml[1])
        csv.export_data_csv(data_list_xml=xml_list, csv_file_name=csv_file)

    @staticmethod
    def export_csv_data_united(arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV.
        """
        path_directory = arg_list[0]
        csv_file = arg_list[1]
        dictionary_with_data = xml.get_data_from_several_xml_files(
            path_of_archives=path_directory)
        if any(dictionary_with_data):
            data_list = []
            for item_xml in dictionary_with_data:
                key = list(item_xml.keys())[0]
                data_list.extend(item_xml[key])

            csv.export_data_csv(data_list_xml=data_list, csv_file_name=csv_file)
            print_info = messages.print_messages_in_colors(
                "\nDatos agregados al archivo →",
                csv_file, color1='blue', color2='yellow')
            print(print_info[0], print_info[1])
            print_total = messages.print_messages_in_colors(
                "Total datos →",
                str(len(data_list)), color1='blue', color2='yellow')
            print(print_total[0], print_total[1])
        else:
            print(messages.print_messages_in_colors("No se encontró ningún archivo XML.", color2='yellow'))

    @staticmethod
    def exporting_multiple_csv_files(arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a varios archivos CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio.
        """
        path_directory = arg_list[0]
        list_of_data = xml.get_data_from_several_xml_files(path_of_archives=path_directory)
        if any(list_of_data):
            for item_xml in list_of_data:
                key = list(item_xml.keys())[0]
                file_name_csv = f"{key}.csv"
                csv.export_data_csv(data_list_xml=item_xml[key], csv_file_name=file_name_csv)
                length_data = len(item_xml[key])
                print_info_export = messages.print_messages_in_colors(
                    "Archivo exportado →",
                    f"{file_name_csv} →",
                    str(length_data), color1='blue', color2='magenta', color3='green')
                print(print_info_export[0], print_info_export[1], print_info_export[2])
        else:
            print(messages.print_messages_in_colors("No se encontró ningún archivo XML.", color='yellow'))

    @staticmethod
    def export_multiple_xml_files(arg_list: list) -> None:
        """ Este método se diseñó para exportar múltiples archivos XML con la lista de datos,
            que reciba del archivo CSV.

        Args:
            arg_list (list): Recibe una lista con el directorio y archivo CSV con los datos a buscar.
        """
        path_directory = arg_list[0]
        csv_file = arg_list[1]
        dictionary_with_data = xml.get_data_from_several_xml_files(
            path_of_archives=path_directory,
            add_path_to_data=True)
        lista_csv = csv.get_csv_data_list(csv_file_name=csv_file)
        if any(dictionary_with_data):
            print_info_total = messages.print_messages_in_colors(
                "\nTotal datos del archivo csv a copiar →",
                str(len(lista_csv)), color1='magenta', color2='green')
            print(print_info_total[0], print_info_total[1])
            (father_dictionary, dict_path) = xml.search_and_filter_data(
                data_dictionary=dictionary_with_data,
                data_list=lista_csv)
            counter = 0
            for key in father_dictionary:
                get_list = [item[key] for item in dictionary_with_data if list(item.keys())[0] == key]
                flatten_list = [item for sublist in get_list for item in sublist]
                csv_file_data_list = father_dictionary[key]
                xml_index = xml.search_the_index_in_the_list(
                    data_list_csv=csv_file_data_list,
                    data_list_xml=flatten_list)
                total_list_index = len(xml_index)
                print_info_index = messages.print_messages_in_colors(
                    "\nTotal indexes encontrados →",
                    str(total_list_index), color1='blue', color2='yellow')
                print(print_info_index[0], print_info_index[1])
                counter += 1
                new_file = f'{key}{counter}.xml'
                total_data = xml.build_xml(
                    xml_file_name=dict_path[key],
                    name_of_the_new_xml_file=new_file,
                    data_index_xml=xml_index)
                print_info_copy = messages.print_messages_in_colors(
                    "Total datos copiados →",
                    str(total_data), color1='blue', color2='yellow')
                print(print_info_copy[0], print_info_copy[1])
                print_info_create = messages.print_messages_in_colors(
                    "Archivo creado →",
                    str(new_file), color1='blue', color2='yellow')
                print(print_info_create[0], print_info_create[1])
        else:
            print(messages.print_messages_in_colors("No se encontró ningún archivo XML.", color='yellow'))

    @staticmethod
    def merge_csv_files(arg_list: list) -> None:
        """ Este método se diseñó para unir todos los archivos CSV que se encuentren en el directorio,
            que le indiquen y exportara un solo archivo CSV con todos los datos.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV,
            que va a almacenar los datos.
        """
        path_directory = arg_list[0]
        csv_file = arg_list[1]
        file_list_in_directory = config.get_the_current_working_directory(
            path_dir=path_directory)
        csv_file_list = [value for value in file_list_in_directory if value.endswith('.csv')]
        if any(csv_file_list):
            join_data = []
            for item_csv in csv_file_list:
                print_info_file = messages.print_messages_in_colors(
                    f"leyendo el archivo →",
                    str(item_csv), color1='blue', color2='yellow')
                print(print_info_file[0], print_info_file[1])
                csv_list = csv.get_csv_data_list(csv_file_name=item_csv)
                join_data.extend(csv_list)

            csv.export_data_csv(data_list_xml=join_data, csv_file_name=csv_file)
            print_info = messages.print_messages_in_colors(
                "Datos agregados al archivo →",
                str(csv_file), color1='blue', color2='yellow')
            print(print_info[0], print_info[1])
            print_info_data = messages.print_messages_in_colors(
                "Total datos →",
                str(len(join_data)), color1='blue', color2='yellow')
            print(print_info_data[0], print_info_data[1])
        else:
            print(messages.print_messages_in_colors(
                f"No hay archivos CSV en el directorio → {path_directory}", color='yellow'))

    @staticmethod
    def search_data_with_parameters(arg_list: list) -> None:
        """ Este método se diseñó para buscar entre "N" cantidad de archivos XML que se encuentren en el directorio,
            que le indiquen y el dato a buscar, luego filtrar y devuelve el dato que esté buscado el usuario,
            por la terminal.

        Args:
            arg_list (list): Recibe una lista con la ruta del directorio y el dato a buscar.
        """
        path_directory = arg_list[0]
        search_data = arg_list[1]
        lista_filtrad = xml.recursive_filter_by_xml_files(path_of_archives=path_directory)
        print(messages.print_messages_in_colors(f"Buscando dato: {search_data}", color='yellow'))
        search = xml.filter_data_in_xml_files(search=search_data, list_of_the_file_paths=lista_filtrad)
        if search is not None:
            [print(f'► {value} → {search[value]}') for value in search]
        else:
            print(messages.print_messages_in_colors(
                "No se encontró el dato, puede que estés buscado un dato desconocido.", color='yellow'))

    @staticmethod
    def lists_of_data_to_compare(arg_list: list) -> None:
        """ Este método se diseñó para comparar dos listas de datos y exportar un archivo CSV,
            con los datos filtrados.

        Args:
            arg_list (list): Recibe dos listas con los datos que se van a comparar y el nombre,
            del archivo que se va a exportar.
        """
        master_csv_file = arg_list[0]
        csv_file = arg_list[1]
        print(messages.print_messages_in_colors("Archivos agregados:", color='blue'))
        print(f"└─>CSV-MASTER → {messages.print_messages_in_colors(basename(master_csv_file), color='green')}")
        csv_list_master = csv.get_csv_data_list(csv_file_name=master_csv_file)
        print_total_master = messages.print_messages_in_colors(
            "└──>Total datos:",
            str(len(csv_list_master)), color1='blue', color2='yellow')
        print(print_total_master[0], print_total_master[1])
        print(f"└─>CSV-compare → {messages.print_messages_in_colors(basename(csv_file), color='yellow')}")
        csv_list_two = csv.get_csv_data_list(csv_file_name=csv_file)
        print_total_csv = messages.print_messages_in_colors(
            "└──>Total datos:",
            str(len(csv_list_two)), color1='blue', color2='yellow')
        print(print_total_csv[0], print_total_csv[1])
        duplicates = csv.compare_lists_of_data(master_list=csv_list_master, data_list_two=csv_list_two)
        if duplicates:
            total_list_csv = len(duplicates)
            print_total_data = messages.print_messages_in_colors(
                "Total datos repetidos:",
                str(total_list_csv), color1='blue', color2='yellow')
            print(print_total_data[0], print_total_data[1])
            csv.export_data_csv(data_list_xml=duplicates, csv_file_name="exporting-duplicates.csv")
        else:
            print(messages.print_messages_in_colors("0 Datos repetidos", color='magenta'))

    @staticmethod
    def remove_xml_values_with_arguments(arg_list: list) -> None:
        """ Este método se diseñó para poder remover los estados de cuenta que se especifiquen,
            en el archivo csv y poder borrarlos del archivo XML.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos XML y CSV.
        """
        csv_file = arg_list[0]
        xml_file = arg_list[1]
        print(messages.print_messages_in_colors("Archivos agregados:", color='blue'))
        print(f"└──>CSV → {messages.print_messages_in_colors(basename(path_dir=csv_file), color='green')}")
        print(f"└──>XML → {messages.print_messages_in_colors(basename(path_dir=xml_file), color='yellow')}\n")
        csv_list = csv.get_csv_data_list(csv_file_name=csv_file)
        total_list_csv = len(csv_list)
        print_total_to_delete = messages.print_messages_in_colors(
            "Total datos csv a eliminar:",
            str(total_list_csv), color1='blue', color2='yellow')
        print(print_total_to_delete[0], print_total_to_delete[1])
        xml.check_and_format_xml(xml_file_name=xml_file)
        xml_list = xml.get_xml_data_list(xml_file_name=xml_file)
        total_list_xml = len(xml_list)
        print_total_xml = messages.print_messages_in_colors(
            "Total estados de cuenta xml:",
            str(total_list_xml), color1='blue', color2='yellow')
        print(print_total_xml[0], print_total_xml[1])
        xml_index = xml.search_the_index_in_the_list(
            data_list_csv=csv_list,
            data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print_total_index = messages.print_messages_in_colors(
            "Total indexes encontrados que se van a eliminar:",
            str(total_list_index), color1='blue', color2='yellow')
        print(print_total_index[0], print_total_index[1])
        total_data_removed = xml.remove_xml_values(
            xml_file_name=xml_file,
            data_index_xml=xml_index)
        print_total_removed = messages.print_messages_in_colors(
            "Total datos eliminados:",
            str(total_data_removed), color1='blue', color2='yellow')
        print(print_total_removed[0], print_total_removed[1])

    @staticmethod
    def print_random_days(arg_list: list) -> None:
        """ Este método se diseñó para poder seleccionar alzar los días de mora.

        Args:
            arg_list (list): Recibe una lista con el nombre del archivo CSV y él,
            número de días a buscar.
        """
        try:
            csv_file = arg_list[0]
            iterations = int(arg_list[1])
            print(messages.print_messages_in_colors("Archivo agregado:", color='blue'))
            print(f"└──>CSV → {messages.print_messages_in_colors(basename(path_dir=csv_file), color='magenta')}")
            print(f"└──>Iterations → {messages.print_messages_in_colors(str(iterations), color='yellow')}\n")
            csv_list = csv.get_csv_data_list(csv_file_name=csv_file)
            print_total_csv = messages.print_messages_in_colors(
                "Total datos en archivo csv:",
                f'{str(len(csv_list))}\n', color1='blue', color2='yellow')
            print(print_total_csv[0], print_total_csv[1])
            csv.select_days(data_list_csv=csv_list, amount=iterations)
        except Exception as error_message_elect_print_random_days:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_messages_in_colors(
                "Posible error: puede ser que ingreso letras y no un número.", color='yellow'))
            print(messages.print_error(
                programmer_error_message="Error al intentar imprimir los días al azar.",
                error_message_from_method=error_message_elect_print_random_days))

    @staticmethod
    def identify_system() -> None:
        """ Este método se diseñó para poder identificar el sistema operativo donde se ejecuta la aplicación,
            y poder limpiar la consola cuando se termine de utilizar la aplicación por medio del menú.
        """
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')

    @staticmethod
    def print_message() -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de guía para el usuario al momento,
            de ejecutar la aplicación por el menú.
        """
        message = str("""
        B I E N V E N I D O

        Nota: verifica que en directorio del proyecto estén los archivos:
        [*.csv y *.xml]
        [Los datos del csv deben estar en una sola columna y solo números]
        [Cargar un archivo csv y xml a la ves]

        [El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]

        """)
        print(re.sub(r' {2,}', '', message))

    @staticmethod
    def print_message_help() -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de ayuda para el usuario y poder,
            ejecutar correctamente la aplicación.
        """
        try:
            path_messages = os.path.join(config.get_base_dir(), 'docs/messages/messages-help.txt')
            with open(path_messages, 'r') as file_with_help_messages:
                help_massages = file_with_help_messages.read()
                print(help_massages)
        except FileNotFoundError as error_help_file:
            print(messages.print_messages_in_colors(
                "El archivo para imprimir las ayudas no se encuentra", color1='red'))
            print_info = messages.print_messages_in_colors(
                f"{error_help_file.args[1]} {error_help_file.filename}",
                "La ubicación del archivo: docs/messages/messages-help.txt",
                color='yellow')
            print(f"{print_info[0]}\n{print_info[1]}")
