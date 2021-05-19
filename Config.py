import os
from typing import Union, List
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
        list_files = os.listdir(path_dir)
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
            filename_yaml: str = 'configXML.yaml'
            basedir = cls.get_base_dir()
            file_list_in_directory = cls.get_the_current_working_directory(basedir)
            search_yaml_file = [value for value in file_list_in_directory if value == filename_yaml]
            path_yaml = os.path.join(basedir, filename_yaml)
            if any(search_yaml_file):
                with open(path_yaml) as file_yaml:
                    yaml_document = yaml.load(file_yaml.read())
            else:
                yaml_document = {
                    'DEV': {
                        'ROOT_XML': 'root',
                        'XML_DOM_PATH': './data/head',
                        'SEARCH_PARAMETERS': ['id', 'number', 'product', 'reference', 'name'],
                        'PRODUCT_PATH': './data/head/product',
                        'TAG_TO_SEARCH': 'id',
                        'TITLE_KEY_VALUE': 'KEY | VALUE'
                    },
                    'PROD': {
                        'ROOT_XML': '',
                        'XML_DOM_PATH': '',
                        'PRODUCT_PATH': '',
                        'SEARCH_PARAMETERS': [],
                        'TAG_TO_SEARCH': '',
                        'TITLE_KEY_VALUE': ''
                    },
                    'RUN': {
                        'MODE': 'DEV'
                    }
                }
                with open(path_yaml, 'w') as create_yaml_file:
                    yaml.dump(yaml_document, create_yaml_file, default_flow_style=False)
            mode = yaml_document['RUN']['MODE']
            data = yaml_document[mode]
            return data
        except Exception as error_in_yaml_configuration:
            print(f"uncaught exception {traceback.format_exc()}")
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
        color_magenta_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color magenta.
        color_end_console (string): Esté atributo se utiliza para guardar Código escape ANSI que finaliza los colores.
        text_bold_console (string): Esté atributo se utiliza para guardar Código escapé ANSI convierte el texto en BOLD.

    Methods:
    -------
        print_message_colors(*args, **kwargs) -> Union[str, List[str]]
        print_error(programmer_error_message: str, error_message_from_method: Exception) -> None
    """
    def __init__(self) -> None:
        """ El constructor de la clase Messages
        """
        self.color_green_console: str = '\33[32m'
        self.color_blue_console: str = '\33[34m'
        self.color_yellow_console: str = '\33[33m'
        self.color_red_console: str = '\033[91m'
        self.color_magenta_console: str = '\033[95m'
        self.color_end_console: str = '\033[0m'
        self.text_bold_console: str = '\33[1m'

    def print_messages_in_colors(self, *args, **kwargs) -> Union[str, List[str]]:
        """ Esté método se diseñó para convertir en colores los textos y luego,
            poderlos imprimir en la terminal.

            NOTA: los argumentos debe ser únicos, si envían argumentos duplicados,
            el que envíen, duplicado retornara solo uno.

        Args:
            *args (str): Texto que se va a cambiar a color.
            **kwargs (Dict[str]): El color que se le aplicara al texto.
        Returns:
            list: Con los textos convertidos en color que le indico el usuario.
        """
        colors = {
            'yellow': self.color_yellow_console,
            'blue': self.color_blue_console,
            'red': self.color_red_console,
            'green': self.color_green_console,
            'magenta': self.color_magenta_console,
            'bold': self.text_bold_console,
            'end': self.color_end_console
        }
        length_args = len(args)
        length_kwargs = len(kwargs.values())
        list_kwargs = list(kwargs.values())
        if length_kwargs < length_args:
            absolute_value = (length_args - length_kwargs)
            extend_values = [list_kwargs[-1]] * absolute_value
            list_kwargs.extend(extend_values)
        text_and_color = dict(zip(args, list_kwargs))
        color_text = []
        for text, color in text_and_color.items():
            color_text.append(f'{colors[color]}{colors["bold"]}{text}{colors["end"]}')
        if len(color_text) <= 1:
            return color_text[0]
        else:
            return color_text

    def print_error(self, programmer_error_message: str, error_message_from_method: Exception) -> None:
        """ Esté método se diseñó para poder imprimir en la terminal de color rojo lo errores de la aplicación,
            romper la ejecución del código.

        Args:
            programmer_error_message (str): Recibe el mensaje que haya dejado el programador para entender,
             el problema que surja.
            error_message_from_method (Exception):  Recibe el mensaje de error que haya lanzado el método.
        """
        print(f"{self.color_red_console}ERROR: {programmer_error_message}{self.color_end_console}")
        exit(f"{self.color_red_console}ERROR: {error_message_from_method}{self.color_end_console}")
