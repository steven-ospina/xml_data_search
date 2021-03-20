import os
import yaml
import traceback
import sys


class Config:
    """
    Está clase está diseñada para cargar todas las configuraciones a la aplicación.

    Attributes:
    ----------

    Methods:
    -------
    get_base_dir() -> str
    get_the_current_working_directory(path_dir: str) -> list
    yaml_configuration(cls) -> dict
    basename(path_dir: str) -> str
    """
    @staticmethod
    def get_base_dir() -> str:
        """ Este método se diseñó para retornar la ruta completa de la aplicación.

        Returns:
            string: Retorna la ruta completa del directorio de la aplicación.
        """
        basedir = os.path.abspath(os.path.dirname(__file__))
        return basedir

    @staticmethod
    def get_the_current_working_directory(path_dir: str) -> list:
        """ Este método se diseñó para poder leer los archivos que están en el directorio,
            donde se esté ejecutando la aplicación

        Args:
            path_dir (str): Recibe la ruta donde están los archivo.

        Returns:
            list: Una lista con los nombres de los archivos del directorio donde se llame la aplicación.
        """
        os.chdir(path_dir)
        cwd = os.getcwd()
        list_files = os.listdir(cwd)
        return list_files

    @classmethod
    def yaml_configuration(cls) -> dict:
        """ Este método se diseñó para leer el archivo YAML, y cargar las rutas y las etiquetas a buscar,
            en el archivo XML, y en caso que el archivo no esté en el directorio de trabajo, el método,
            también se encargara de crear la estructura y el archivo.

        Returns:
            dict: Retorna un diccionario con las rutas y etiquetas a buscar.
        """
        try:
            filename_yaml = 'configXML.yaml'
            basedir = cls.get_base_dir()
            file_list_in_directory = os.listdir(basedir)
            search_yaml_file = [value for value in file_list_in_directory if value == filename_yaml]
            path_yaml = os.path.join(basedir, filename_yaml)
            if any(search_yaml_file):
                with open(path_yaml) as file_yaml:
                    yaml_document = yaml.load(file_yaml.read())
            else:
                yaml_document = {
                    'dev': {
                        'ROOT_XML': 'root',
                        'XML_DOM_PATH': './data/head',
                        'ID': './head/id',
                        'NUMBER': './head/number',
                        'PRODUCT': './head/product',
                        'REFERENCE': './head/reference',
                        'NAME': './head/name',
                        'PRODUCT_PATH': './data/head/product',
                        'TAG_TO_SEARCH': 'id'
                    },
                    'prod': {
                        'ROOT_XML': '',
                        'XML_DOM_PATH': '',
                        'ID': '',
                        'NUMBER': '',
                        'PRODUCT': '',
                        'REFERENCE': '',
                        'NAME': '',
                        'PRODUCT_PATH': '',
                        'TAG_TO_SEARCH': ''
                    },
                    'run': {
                        'mode': 'dev'
                    }
                }
                with open(path_yaml, 'w') as create_yaml_file:
                    yaml.dump(yaml_document, create_yaml_file, default_flow_style=False)
            mode = yaml_document['run']['mode']
            data = yaml_document[mode]
            return data

        except Exception as error_in_yaml_configuration:
            print(f"uncaught exception {traceback.format_exc()}")
            print(f"Error al intentar cargar el archivo {filename_yaml}")
            sys.exit(f"llave con error: {error_in_yaml_configuration}")

    @staticmethod
    def basename(path_dir: str) -> str:
        """ Este método se diseñó para leer la ruta del archivo y devolver solo el nombre del archivo,
            sin la ruta completa.

        Args:
            path_dir (str): Recibe la ruta donde están el archivo.

        Returns:
            str: Retorna el nombre del archivo sin la ruta absoluta.
        """
        try:
            return os.path.basename(path_dir)
        except TypeError as error_in_basename:
            print(f"uncaught exception {traceback.format_exc()}")
            print(error_in_basename)
            print(f"Error al intentar devolver el nombre del archivo {path_dir}")


class Messages:
    """
    Está clase está diseñada para imprimir mensajes en la terminal con colores.

    Attributes:
    ----------
        color_green_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color verde.
        color_blue_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color azul.
        color_yellow_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color amarillo.
        color_red_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color rojo.
        color_red_magenta (string): Esté atributo se utiliza para guardar Código escapé ANSI de color magenta.
        color_end_console (string): Esté atributo se utiliza para guardar Código escape ANSI que finaliza los colores.
        text_bold_console (string): Esté atributo se utiliza para guardar Código escapé ANSI convierte el texto en BOLD.

    Methods:
    -------
        print_message_yellow(message: str) -> str
        print_message_green(message: str) -> str
        print_message_blue(message: str) -> str
        print_message_red(message: str) -> str
        print_message_magenta(message: str) -> str
        print_message_with_blue_and_yellow_colors(message_one: str, message_two: str) -> str
        print_error(programmer_error_message: str, error_message_from_method: Exception) -> None
    """
    def __init__(self) -> None:
        """ El constructor de la clase Messages
        """
        self.color_green_console: str = '\33[32m'
        self.color_blue_console: str = '\33[34m'
        self.color_yellow_console: str = '\33[33m'
        self.color_red_console: str = '\033[91m'
        self.color_red_magenta: str = '\033[95m'
        self.color_end_console: str = '\033[0m'
        self.text_bold_console: str = '\33[1m'

    def print_message_yellow(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color amarillo.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color amarillo.

        Returns:
            str: El mensaje que envió el usuario, pero en color amarillo.
        """
        return f"{self.color_yellow_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_green(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color verde.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color verde.

        Returns:
            str: El mensaje que envió el usuario, pero en color verde.
        """
        return f"{self.color_green_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_blue(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color azul.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color azul.

        Returns:
            str: El mensaje que envió el usuario, pero en color azul.
        """
        return f"{self.color_blue_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_red(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color rojo.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color rojo.

        Returns:
            str: El mensaje que envió el usuario, pero en color rojo.
        """
        return f"{self.color_red_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_magenta(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color magenta.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color magenta.

        Returns:
            str: El mensaje que envió el usuario, pero en color magenta.
        """
        return f"{self.color_red_magenta}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_with_blue_and_yellow_colors(self, message_one: str, message_two: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color azul y amarillo.

        Args:
            message_one (str): Recibe el mensaje que se va a convertir a color azul.
            message_two (str): Recibe el mensaje que se va a convertir a color amarillo.

        Returns:
            str: El mensaje que envió el usuario, pero en color azul y amarillo.
        """
        message_one = self.print_message_blue(message=message_one)
        message_two = self.print_message_yellow(message=message_two)
        return f'{message_one} {message_two}'

    def print_error(self, programmer_error_message: str, error_message_from_method: Exception) -> None:
        """ Esté método se diseñó para poder imprimir en la terminal de color rojo lo errores de la aplicación, romper la ejecución del código.

        Args:
            programmer_error_message (str): Recibe el mensaje que haya dejado el programador para entender el problema que surja.
            error_message_from_method (Exception):  Recibe el mensaje de error que haya lanzado el método.
        """
        print(f"{self.color_red_console}ERROR: {programmer_error_message}{self.color_end_console}")
        exit(f"{self.color_red_console}ERROR: {error_message_from_method}{self.color_end_console}")
