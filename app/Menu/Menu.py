from ..Csv.Csv import Csv
from ..Xml.Xml import Xml
from Config import Messages, Config
import os
import traceback


class Menu:
    """
    Está clase fue diseñada para poder mostrar al usuario un menú para utilizar,
    la aplicación, o poder ejecutar la aplicación por medio de argumentos que,
    recibe la aplicación.

    Attributes:
    ----------
        _flag (bool): Esté atributo se utiliza para poder ejecutar el menú,
        que tiene la aplicación.
        csv (class): Esté atributo se utiliza para poder instaciar la clase Csv,
        y poder invocar los métodos.
        xml (class): Esté atributo se utiliza para poder instancia la clase Xml,
        y poder invocar los métodos.
        messages (class): Esté atributo se utiliza para poder instancia la clase Messages,
        y poder invocar los métodos.
        BASE_DIR (class): Esté atributo se utiliza para poder instancia la clase Config,
        y importar la ruta raíz del proyecto.
        PATH_DIR (class): Esté atributo se utiliza para poder instancia la clase Config,
        y instancia el método que obtiene los archivos del directorio que le indiquen.

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
        self.BASE_DIR = Config().get_base_dir()
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
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        BASENAME = self.PATH_DIR.basename
        print(MESSAGES.print_message_blue(message="Archivos agregados:"))
        print(f"* CSV: {MESSAGES.print_message_yellow(message=BASENAME(path_dir=arg_list[1]))}")
        print(f"* XML: {MESSAGES.print_message_green(message=BASENAME(path_dir=arg_list[2]))}")
        print(f"* Name of the new xml file: {MESSAGES.print_message_magenta(message=BASENAME(path_dir=arg_list[3]))}\n")
        csv_list = CSV.get_csv_data_list(csv_file_name=arg_list[1])
        total_list_csv = len(csv_list)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total datos en archivo csv:",
            message_two=str(total_list_csv)))
        XML.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = XML.get_xml_data_list(xml_file_name=arg_list[2])
        total_list_xml = len(xml_list)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total datos en archivo xml:",
            message_two=str(total_list_xml)))
        xml_index = XML.search_the_index_in_the_list(
            data_list_csv=csv_list,
            data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total indexes encontrados:",
            message_two=str(total_list_index)))
        total_data = XML.build_xml(
            xml_file_name=arg_list[2],
            name_of_the_new_xml_file=arg_list[3],
            data_index_xml=xml_index)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total datos copiados:",
            message_two=str(total_data)))

    # Método para formatear archivos xml por medio de argumentos por linea de comando
    def format_xml_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder verificar si el archivo XML está formateado,
            si no está formateado le dará un formato para poder leer los datos y si es lo contrario,
            no hará nada.
        Args:
            arg_list (list): Recibe una lista con el nombre del archivo xml y poder dar formato.
        """
        MESSAGES = self.messages
        XML = self.xml
        BASENAME = self.PATH_DIR.basename
        print(MESSAGES.print_message_blue(message="Archivo agregado para formatear:"))
        print(f"XML → {MESSAGES.print_message_green(message=BASENAME(path_dir=arg_list[2]))}")
        XML.check_and_format_xml(xml_file_name=arg_list[2])

    # Método para exportar los estados de cuenta a un archivo csv por medio de argumentos por linea de comando
    def export_data_csv_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            el archivo XML que se esté trabajando y poder exportarlos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos XML y CSV.
        """
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        BASENAME = self.PATH_DIR.basename
        print(MESSAGES.print_message_blue(message="Archivos agregados:"))
        print(f"XML → {MESSAGES.print_message_yellow(message=BASENAME(path_dir=arg_list[2]))}")
        print(f"CSV → {MESSAGES.print_message_green(message=BASENAME(path_dir=arg_list[3]))}\n")
        XML.check_and_format_xml(xml_file_name=arg_list[2])
        xml_list = XML.get_xml_data_list(xml_file_name=arg_list[2])
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total estados de cuenta xml:",
            message_two=str(len(xml_list))))
        CSV.export_data_csv(data_list_xml=xml_list, csv_file_name=arg_list[3])

    def export_csv_data_united(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a un archivo CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV.
        """
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        dictionary_with_data = XML.get_data_from_several_xml_files(
            path_of_archives=arg_list[2])
        if any(dictionary_with_data):
            data_list = []
            for item_xml in dictionary_with_data:
                key = list(item_xml.keys())[0]
                data_list.extend(item_xml[key])

            CSV.export_data_csv(data_list_xml=data_list, csv_file_name=arg_list[3])
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="\nDatos agregados al archivo →",
                message_two=arg_list[3]))
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="Total datos →",
                message_two=str(len(data_list))))
        else:
            print(MESSAGES.print_message_yellow(message="No se enctor ningún archivo xml"))

    def exporting_multiple_csv_files(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar todos los números de estados de cuenta que están,
            en los archivos XML que se esté en el directorio que se le indique y poder exportar,
            todos estos datos a varios archivos CSV.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio.
        """
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        list_of_data = XML.get_data_from_several_xml_files(path_of_archives=arg_list[2])
        if any(list_of_data):
            for item_xml in list_of_data:
                key = list(item_xml.keys())[0]
                file_name_csv = f"{key}.csv"
                CSV.export_data_csv(data_list_xml=item_xml[key], csv_file_name=file_name_csv)
                length_data = len(item_xml[key])
                print(MESSAGES.print_message_with_blue_and_yellow_colors(
                    message_one=f"Archivo Exportado → {file_name_csv}",
                    message_two=str(length_data)))
        else:
            print(MESSAGES.print_message_yellow(message="No se enctor ningún archivo xml"))

    def export_multiple_xml_files(self, arg_list: list) -> None:
        """ Este método se diseñó para exportar múltiples archivos XML con la lista de datos,
            que reciba del archivo CSV.

        Args:
            arg_list (list): Recibe una lista con el directorio y archivo CSV con los datos a buscar.
        """
        print(self.filter_directory_by_xml_and_csv_files())
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        dictionary_with_data = XML.get_data_from_several_xml_files(
            path_of_archives=arg_list[2],
            add_path_to_data=True)
        lista_csv = CSV.get_csv_data_list(csv_file_name=arg_list[3])
        if any(dictionary_with_data):
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="\nTotal datos del archivo csv a copiar →",
                message_two=str(len(lista_csv))))
            (father_dictionary, dict_path) = XML.search_and_filter_data(
                data_dictionary=dictionary_with_data,
                data_list=lista_csv)
            counter = 0
            for key in father_dictionary:
                get_list = [item[key] for item in dictionary_with_data if list(item.keys())[0] == key]
                flatten_list = [item for sublist in get_list for item in sublist]
                csv_file_data_list = father_dictionary[key]
                xml_index = XML.search_the_index_in_the_list(
                    data_list_csv=csv_file_data_list,
                    data_list_xml=flatten_list)
                total_list_index = len(xml_index)
                print(MESSAGES.print_message_with_blue_and_yellow_colors(
                    message_one="\nTotal indexes encontrados →",
                    message_two=str(total_list_index)))
                counter += 1
                new_file = f'{key}{counter}.xml'
                total_data = XML.build_xml(
                    xml_file_name=dict_path[key],
                    name_of_the_new_xml_file=new_file,
                    data_index_xml=xml_index)
                print(MESSAGES.print_message_with_blue_and_yellow_colors(
                    message_one="Total datos copiados →",
                    message_two=str(total_data)))
                print(MESSAGES.print_message_with_blue_and_yellow_colors(
                    message_one="Archivo creado →",
                    message_two=str(new_file)))
        else:
            print(MESSAGES.print_message_yellow(message="No se enctor ningún archivo xml"))

    def merge_csv_files(self, arg_list: list) -> None:
        """ Este método se diseñó para unir todos los archivos CSV que se encuentren en el directorio,
            que le indiquen y exportara un solo archivo CSV con todos los datos.

        Args:
            arg_list (list): Recibe una lista con ruta del directorio y el nombre del archivo CSV,
            que va a almacenar los datos.
        """
        MESSAGES = self.messages
        file_list_in_directory = self.PATH_DIR.get_the_current_working_directory(
            path_dir=arg_list[2])
        csv_file_list = [value for value in file_list_in_directory if value.endswith('.csv')]
        if any(csv_file_list):
            join_data = []
            for item_csv in csv_file_list:
                print(MESSAGES.print_message_with_blue_and_yellow_colors(
                    message_one=f"leyendo el archivo →",
                    message_two=str(item_csv)))
                csv_list = self.csv.get_csv_data_list(csv_file_name=item_csv)
                join_data.extend(csv_list)

            self.csv.export_data_csv(data_list_xml=join_data, csv_file_name=arg_list[3])
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="Datos agregados al archivo →",
                message_two=str(arg_list[3])))
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="Total datos →",
                message_two=str(len(join_data))))
        else:
            print(MESSAGES.print_message_yellow(f"No hay archivos CSV en el directorio → {arg_list[2]}"))

    def search_data_with_parameters(self, arg_list: list) -> None:
        """ Este método se diseñó para buscar entre "N" cantidad de archivos XML que se encuentren en el directorio,
            que le indiquen y el dato a buscar, luego filtrar y devuelve el dato que esté buscado el usuario,
            por la terminal.

        Args:
            arg_list (list): Recibe una lista con la ruta del directorio y el dato a buscar.
        """
        lista_filtrad = self.xml.recursive_filter_by_xml_files(path_of_archives=arg_list[2])
        print(self.messages.print_message_yellow(message=f"Buscando dato: {arg_list[3]}"))
        search = self.xml.filter_data_in_xml_files(search=arg_list[3], list_of_the_file_paths=lista_filtrad)
        if search is not None:
            [print(f'► {value} → {search[value]}') for value in search]
        else:
            print("No se encontró el dato, puede que estés buscado un dato desconocido.")

    def lists_of_data_to_compare(self, arg_list: list) -> None:
        """ Este método se diseñó para comparar dos listas de datos y exportar un archivo CSV,
            con los datos filtrados.

        Args:
            arg_list (list): Recibe dos listas con los datos que se van a comparar y el nombre,
            del archivo que se va a exportar.
        """
        MESSAGES = self.messages
        CSV = self.csv
        print(MESSAGES.print_message_blue(message="Archivos agregados:"))
        print(f"* CSV-MASTER: {MESSAGES.print_message_green(message=arg_list[2])}")
        csv_list_master = CSV.get_csv_data_list(csv_file_name=arg_list[3])
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="└──>Total datos:",
            message_two=str(len(csv_list_master))))
        print(f"* CSV-compare: {MESSAGES.print_message_yellow(message=arg_list[3])}")
        csv_list_two = CSV.get_csv_data_list(csv_file_name=arg_list[2])
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="└──>Total datos:",
            message_two=str(len(csv_list_two))))
        duplicates = CSV.compare_lists_of_data(master_list=csv_list_master, data_list_two=csv_list_two)
        if duplicates != []:
            total_list_csv = len(duplicates)
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="Total datos repetidos:",
                message_two=str(total_list_csv)))
            CSV.export_data_csv(data_list_xml=duplicates, csv_file_name="exporting-duplicates.csv")
        else:
            print(MESSAGES.print_message_blue(message="0 Datos repetidos"))

    def remove_xml_values_with_arguments(self, arg_list: list) -> None:
        """ Este método se diseñó para poder remover los estados de cuenta que se especifiquen,
            en el archivo csv y poder borrarlos del archivo XML.

        Args:
            arg_list (list): Recibe una lista con los nombres de los archivos XML y CSV.
        """
        MESSAGES = self.messages
        CSV = self.csv
        XML = self.xml
        BASENAME = self.PATH_DIR.basename
        print(MESSAGES.print_message_blue(message="Archivos agregados:"))
        print(f"CSV → {MESSAGES.print_message_green(message=BASENAME(path_dir=arg_list[2]))}")
        print(f"XML → {MESSAGES.print_message_yellow(message=BASENAME(path_dir=arg_list[3]))}\n")
        csv_list = CSV.get_csv_data_list(csv_file_name=arg_list[2])
        total_list_csv = len(csv_list)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total datos csv a eliminar:",
            message_two=str(total_list_csv)))
        XML.check_and_format_xml(xml_file_name=arg_list[3])
        xml_list = XML.get_xml_data_list(xml_file_name=arg_list[3])
        total_list_xml = len(xml_list)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total estados de cuenta xml:",
            message_two=str(total_list_xml)))
        xml_index = XML.search_the_index_in_the_list(
            data_list_csv=csv_list,
            data_list_xml=xml_list)
        total_list_index = len(xml_index)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total indexes encontrados que se van a eliminar:",
            message_two=str(total_list_index)))
        total_data_removed = XML.remove_xml_values(
            xml_file_name=arg_list[3],
            data_index_xml=xml_index)
        print(MESSAGES.print_message_with_blue_and_yellow_colors(
            message_one="Total datos eliminados:",
            message_two=str(total_data_removed)))

    def print_random_days(self, arg_list: list) -> None:
        """ Este método se diseñó para poder seleccionar alzar los días de mora.

        Args:
            arg_list (list): Recibe una lista con el nombre del archivo CSV y él,
            número de días a buscar.
        """
        try:
            MESSAGES = self.messages
            CSV = self.csv
            BASENAME = self.PATH_DIR.basename
            print(MESSAGES.print_message_blue(message="Archivo agregado:"))
            print(f"* CSV: {MESSAGES.print_message_magenta(message=BASENAME(path_dir=arg_list[2]))}")
            iterations = int(arg_list[3])
            print(f"* Iterations: {MESSAGES.print_message_yellow(message=str(iterations))}\n")
            csv_list = CSV.get_csv_data_list(csv_file_name=arg_list[2])
            print(MESSAGES.print_message_with_blue_and_yellow_colors(
                message_one="Total datos en archivo csv:",
                message_two=f'{str(len(csv_list))}\n'))
            CSV.select_days(data_list_csv=csv_list, amount=iterations)
        except Exception as error_message_elect_print_random_days:
            print(f"uncaught exception {traceback.format_exc()}")
            print(MESSAGES.print_message_yellow(
                message="Posible error: puede ser que ingreso letras y no un número."))
            print(MESSAGES.print_error(
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
        print('B I E N V E N I D O\n')
        print('Nota: verifica que en directorio del proyecto estén los archivos:')
        print('[*.csv y *.xml]')
        print('[Los datos del csv deben estar en una sola columna y solo números]')
        print('[Cargar un archivo csv y xml a la ves]\n')
        print('[El archivo [.xml] debe estar formateado para que el sistema lo pueda procesar]\n')

    def print_message_help(self) -> None:
        """ Este método se diseñó para imprimir un mensaje en modo de ayuda para el usuario y poder,
            ejecutar correctamente la aplicación.
        """
        MESSAGES = self.messages
        try:
            path_messages = os.path.join(self.BASE_DIR, 'docs/messages/messages-help.txt')
            with open(path_messages, 'r') as file_with_help_messages:
                help_massages = file_with_help_messages.read()
                print(help_massages)
        except FileNotFoundError as error_help_file:
            print(MESSAGES.print_message_red(message="El archivo para imprimir las ayudas no se encuentra"))
            print(MESSAGES.print_message_yellow(message=f"{error_help_file.args[1]} {error_help_file.filename}"))
            print(MESSAGES.print_message_yellow(message="La ubicación del archivo: docs/messages/messages-help.txt"))
